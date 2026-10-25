# 📚 Multi-PDF Chatbot Using RAG, Gemini, Groq & Streamlit

An AI-powered chatbot that allows users to upload multiple PDF documents, ask questions in natural language, and receive context-aware answers based on the documents' content using **Retrieval-Augmented Generation (RAG)**.

## 📌 Project Overview

Imagine you have 10 PDF documents, each containing 100 pages, and you need to find the answer to one specific question. Would you open every PDF, search through hundreds of pages, and read everything manually? 🤔

What if you could simply upload all your PDFs, ask a question in plain English, and get an answer based on their content within seconds?

**That is exactly what this project does!**

The Multi-PDF Chatbot combines document processing, vector embeddings, semantic search, and Large Language Models (LLMs) to make information retrieval from multiple PDF files faster and easier.

## 🎯 Project Goal

The goal of this project is to develop an AI-powered Multi-PDF Chatbot using **Retrieval-Augmented Generation (RAG)** and **Streamlit**. The application enables users to upload multiple PDF documents and interact with their content through a simple, user-friendly chat interface.

The system uses **Google Gemini embeddings** to convert document chunks into vector representations, **FAISS** to efficiently retrieve relevant information, and a **Groq-hosted LLM** to generate answers grounded in the retrieved context.

## ✨ Key Features

- 📄 **Multiple PDF Uploads:** Upload multiple PDF documents simultaneously.
- 📝 **Text Extraction:** Extract text from uploaded PDF files.
- ✂️ **Text Chunking:** Split large documents into smaller, manageable chunks.
- 🧠 **Gemini Embeddings:** Convert text chunks into vector embeddings.
- 🔍 **Semantic Search:** Retrieve relevant document content based on user questions.
- ⚡ **FAISS Vector Search:** Efficiently search and retrieve similar document chunks.
- 🤖 **LLM-Powered Responses:** Generate context-aware answers using a Groq-hosted language model.
- 💬 **Interactive Chatbot:** Ask questions in natural language through a Streamlit interface.
- 📚 **Context-Aware Retrieval:** Generate responses using information retrieved from the uploaded documents.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Retrieval-Augmented Generation (RAG) | Ground LLM responses in retrieved document content |
| Google Gemini Embeddings | Generate vector representations of text |
| FAISS | Vector similarity search and retrieval |
| Groq API | Access a hosted LLM for answer generation |
| PDF Processing Library | Extract text from PDF documents |
| LangChain (if used) | Document processing and RAG pipeline integration |

## 🔄 How It Works

1. **Upload PDFs:** The user uploads multiple PDF documents through the Streamlit interface.
2. **Extract Text:** The application extracts text from each PDF.
3. **Split Text into Chunks:** The extracted text is divided into smaller chunks for efficient retrieval.
4. **Generate Embeddings:** Gemini embeddings convert the text chunks into numerical vector representations.
5. **Build the Vector Index:** FAISS indexes the embeddings to support efficient similarity searches.
6. **Ask a Question:** The user enters a question in the chatbot interface.
7. **Retrieve Relevant Context:** FAISS retrieves the document chunks most relevant to the question.
8. **Generate an Answer:** The Groq-hosted LLM uses the retrieved context to generate a relevant response.
9. **Display the Response:** Streamlit displays the generated answer to the user.

10. ![Uploading image.png…]()


## 🏗️ System Architecture

```text
        Multiple PDF Documents
                  |
                  v
          Extract PDF Text
                  |
                  v
          Split into Chunks
                  |
                  v
       Gemini Text Embeddings
                  |
                  v
          FAISS Vector Index
                  |
                  |
User Question --->|
       |
       v
Generate Query Embedding
       |
       v
Retrieve Relevant Chunks
       |
       v
 Combine Question + Context
       |
       v
    Groq-hosted LLM
       |
       v
  Contextual Answer
       |
       v
  Streamlit Chat UI
```

## 📂 Project Structure

```text
Multi-PDF-Chatbot/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # API keys (not committed)
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

*Note: Update the project structure to match your actual repository files.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Multi-PDF-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the project root directory and add your API credentials:

```env
GOOGLE_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder values with your actual API keys. Never commit your API keys or `.env` file to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the chatbot.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key for Google Gemini embeddings |
| `GROQ_API_KEY` | API key for the Groq-hosted LLM |

*The environment variable names must match those used in your application code.*

## 🎯 Expected Outcome

The final application provides a conversational interface where users can:

- Upload multiple PDF documents.
- Ask questions about the uploaded documents.
- Retrieve relevant information without manually searching every file.
- Receive AI-generated answers based on retrieved document content.
- Explore large collections of documents more efficiently.

## 🚀 Use Cases

- 📖 Research papers and academic documents
- 🎓 Study materials and educational PDFs
- 📑 Business reports and documentation
- ⚖️ Legal documents and policy manuals
- 📊 Financial reports and analytical documents
- 📚 E-books, manuals, and technical documentation

## 🔮 Future Improvements

- Display source documents and page numbers for answers.
- Support additional file formats such as DOCX and TXT.
- Add persistent vector storage.
- Implement chat history and conversational memory.
- Improve retrieval with reranking and hybrid search.
- Deploy the application to Streamlit Community Cloud or another hosting platform.
- Add authentication and document-level access controls.

## 📁 Project Resources

Access the project resources and reference materials here:

🔗 [Google Drive — Project Resources](https://drive.google.com/drive/folders/1WBAFIZYcAJ757Nn1jZuZYp4WuLWeiyhX?usp=sharing)

## 👨‍💻 Author

**Krishnakant Awasthi**

- GitHub: [Krishnakant Awasthi](https://github.com/KrishnakantAwasthi)
- LinkedIn: [Krishnakant Awasthi](https://www.linkedin.com/in/krishnakantawasthi)

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

---

**Built with Python, Streamlit, Gemini Embeddings, FAISS, Groq, and Retrieval-Augmented Generation (RAG).**
