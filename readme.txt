
1. Create a virtual environment

# mac
python3 -m venv .venv
source .venv/bin/activate

2. Add dependencies to requirements.txt

streamlit
python-dotenv
pypdf
langchain-core
langchain-classic
langchain-community
langchain-text-splitters
langchain-google-genai
langchain-groq
faiss-cpu

# save file and run
pip install -r requirements.txt


3. Configure API keys

Create .env in the project root and add:

GOOGLE_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key

4. #Run the project
#In the VS Code terminal:

streamlit run app.py