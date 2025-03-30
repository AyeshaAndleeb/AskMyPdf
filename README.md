# AskMyPdf 📝🤖

## 📌 Project Overview
**AskMyPdf** is a **Retrieval-Augmented Generation (RAG) based chatbot** that allows users to upload a PDF document, extract its contents, store them in a **FAISS vector database**, and interact with an **open-source LLM** using the **Groq API**. The chatbot retrieves relevant context from the uploaded document and generates AI-powered responses.

## 🚀 Features
- 📂 **Upload PDF Files**
- 🔍 **Extract and Chunk Text**
- 🧠 **Generate Embeddings using HuggingFace**
- 🗃 **Store and Retrieve using FAISS (Open-Source Vector DB)**
- 🤖 **Query LLM using Groq API**
- 🌍 **Deployable on Hugging Face Spaces & Local (VS Code)**

---

## 🛠 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **Vector Database:** FAISS
- **LLM API:** Groq API
- **Deployment:** Hugging Face Spaces / VS Code

---

## 🔧 Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/AyeshaAndleeb/AskMyPdf.git
cd AskMyPdf
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key
Create a `.env` file and add your **Groq API Key**:
```sh
GROQ_API_KEY=your_actual_api_key
```

### 4️⃣ Run the App (Locally in VS Code)
```sh
streamlit run app.py
```

### 5️⃣ Deploy on Hugging Face Spaces
1. Upload `app.py` and `requirements.txt` to your **Hugging Face Space**.
2. Click **Restart Space** to install dependencies.
3. The app will be live in a few minutes!

---

## 📂 Project Structure
```
📁 AskMyPdf
│── 📄 app.py              # Main application code
│── 📄 requirements.txt     # Python dependencies
│── 📄 .env                 # API key storage (Not committed to GitHub)
│── 📄 README.md            # Project documentation
```

---

## ✨ How It Works
1️⃣ **User uploads a PDF** 📂  
2️⃣ **Text is extracted and split into chunks** 📄  
3️⃣ **Embeddings are created and stored in FAISS** 🔍  
4️⃣ **User asks a question** ❓  
5️⃣ **Relevant context is retrieved** from FAISS 🧠  
6️⃣ **Groq API generates a response** 🤖  

---

## 🛠 Troubleshooting
### 🔴 `ModuleNotFoundError: No module named 'faiss'`
✅ Run:
```sh
pip install faiss-cpu
```

### 🔴 `ValueError: File path is not a valid file or URL`
✅ Ensure the uploaded file is properly **saved locally** before processing.

---

## 🤝 Contributing
Want to improve **AskMyPdf**? Feel free to **fork the repo**, create a **new branch**, and submit a **pull request**!

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 📬 Contact
🔗 **GitHub**: [yourgithub](https://github.com/AyeshaAndleeb)  
🔗 **LinkedIn**: [yourlinkedin](https://linkedin.com/in/ayesha-andleeb)  
📧 **Email**: ayeshaandleeb129@email.com
