

GOOGLE_API_KEY="AQ.Ab8RN6KGLtch_ydnbMVRhCDLG8M9SB7mah1b1X45atix5F8x3w"
GROQ_API_KEY="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"

"""**Step 5: Add the chatbot code**

create app.py and add code

"""

# Import necessary libraries
import os
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.question_answering import load_qa_chain
from langchain_core.prompts import PromptTemplate

# Load API keys
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not GROQ_API_KEY:
    st.error("Please add GROQ_API_KEY to your .env file.")
    st.stop()

if not GEMINI_API_KEY:
    st.error("Please add GEMINI_API_KEY to your .env file.")
    st.stop()


# Extract text from PDFs
def get_pdf_text(uploaded_files):
    text = ""

    for file in uploaded_files:
        pdf_reader = PdfReader(file)

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

    return text


# Split text into chunks
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    return splitter.split_text(text)


# Create Gemini embeddings
@st.cache_resource
def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=GEMINI_API_KEY
    )


# Create FAISS vector store
def get_vector_store(text_chunks):
    embeddings = get_embeddings()

    vector_store = FAISS.from_texts(
        texts=text_chunks,
        embedding=embeddings
    )

    vector_store.save_local("faiss_index")

    return vector_store


# Create question-answering chain WITH MEMORY
def get_conversational_chain():
    prompt_template = """
    You are a helpful PDF assistant.

    Use the conversation history to understand follow-up questions.
    Answer using the retrieved PDF context.
    If the answer is not available in the context, say:
    "Answer is not available in the context."

    Conversation History:
    {chat_history}

    PDF Context:
    {context}

    Current Question:
    {question}

    Answer:
    """

    model = ChatGroq(
        model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        temperature=0.3,
        api_key=GROQ_API_KEY
    )

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question", "chat_history"]
    )

    return load_qa_chain(
        model,
        chain_type="stuff",
        prompt=prompt
    )


# Chat with PDFs using conversation memory
def chat_with_pdf(question):
    embeddings = get_embeddings()

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Retrieve relevant PDF chunks
    docs = db.similarity_search(question, k=4)

    # MEMORY: Get the last 5 question-answer pairs
    previous_messages = st.session_state.history[-5:]

    chat_history = ""

    for old_question, old_answer in previous_messages:
        chat_history += f"User: {old_question}\n"
        chat_history += f"Assistant: {old_answer}\n"

    # Generate answer using PDF context and conversation history
    chain = get_conversational_chain()

    result = chain.invoke({
        "input_documents": docs,
        "question": question,
        "chat_history": chat_history
    })

    return result["output_text"]


# Streamlit interface
st.title("💬 Multi-PDF Chatbot Using RAG and Streamlit")
st.caption("Gemini Embeddings | FAISS | Groq | Conversation Memory")

with st.sidebar:
    st.header("📄 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Process PDFs"):
        if not uploaded_files:
            st.warning("Please upload at least one PDF.")
        else:
            try:
                with st.spinner("Processing PDFs..."):
                    raw_text = get_pdf_text(uploaded_files)

                    if not raw_text.strip():
                        st.error("No readable text found in the PDFs.")
                    else:
                        chunks = get_text_chunks(raw_text)
                        get_vector_store(chunks)

                        st.session_state["pdf_processed"] = True
                        st.session_state.history = []

                        st.success(
                            f"Successfully processed {len(chunks)} chunks!"
                        )

            except Exception as error:
                st.error(f"PDF processing failed: {error}")


# Initialize conversation memory
if "history" not in st.session_state:
    st.session_state.history = []

st.header("Ask Questions About Your PDFs")

# Display previous conversation
for q, a in st.session_state.history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Assistant:** {a}")

question = st.text_input(
    "Your Question",
    key="current_question"
)

if st.button("Submit") and question.strip():
    if not st.session_state.get("pdf_processed", False):
        st.warning("Please upload and process your PDFs first.")
    else:
        try:
            with st.spinner("Thinking..."):
                answer = chat_with_pdf(question)

            # Save the new conversation in memory
            st.session_state.history.append((question, answer))

            # Clear the input and refresh the interface
            st.rerun()

        except Exception as error:
            st.error(f"Could not generate answer: {error}")

# Clear conversation memory
if st.button("Clear Chat History"):
    st.session_state.history = []
    st.rerun()
