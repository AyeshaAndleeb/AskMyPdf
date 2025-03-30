import os
import streamlit as st
import tempfile
import chromadb
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from groq import Groq
from dotenv import load_dotenv
import traceback

# Load environment variables
load_dotenv()

# Check for required environment variables
if not os.getenv("GROQ_API_KEY"):
    st.error("Please set the GROQ_API_KEY environment variable")
    st.stop()

# Initialize Groq API Client
try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except Exception as e:
    st.error(f"Failed to initialize Groq client: {str(e)}")
    st.stop()

# Initialize Hugging Face embeddings model (open-source)
try:
    embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
except Exception as e:
    st.error(f"Failed to initialize embeddings model: {str(e)}")
    st.stop()

# Initialize ChromaDB client
try:
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    vector_store = Chroma(embedding_function=embeddings, client=chroma_client)
except Exception as e:
    st.error(f"Failed to initialize ChromaDB: {str(e)}")
    st.stop()

# Streamlit App UI
st.title("📄 RAG-Based PDF Chatbot (ChromaDB)")
st.write("Upload a PDF, ask questions, and get AI-powered responses!")

# Initialize session state for storing processed documents
if 'processed_documents' not in st.session_state:
    st.session_state.processed_documents = False

# File Upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_pdf_path = temp_file.name

        # Load PDF
        loader = PyPDFLoader(temp_pdf_path)
        documents = loader.load()

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(documents)

        # Convert chunks into embeddings
        texts = [chunk.page_content for chunk in chunks]
        vector_store.add_texts(texts)

        st.session_state.processed_documents = True
        st.success("PDF processed successfully! Now you can ask questions.")

    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
        st.error(traceback.format_exc())
    finally:
        # Clean up temporary file
        try:
            os.unlink(temp_pdf_path)
        except Exception as e:
            st.warning(f"Could not delete temporary file: {str(e)}")

    # User Input for Query
    query = st.text_input("Ask a question about the PDF:")
    
    if query and st.session_state.processed_documents:
        try:
            # Retrieve similar documents
            docs = vector_store.similarity_search(query, k=3)
            context = "\n".join([doc.page_content for doc in docs])

            # Generate response using Groq API
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}],
                model="llama-3-8b-instruct"  # Open-source model from Groq
            )

            response = chat_completion.choices[0].message.content
            st.subheader("🤖 AI Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            st.error(traceback.format_exc())