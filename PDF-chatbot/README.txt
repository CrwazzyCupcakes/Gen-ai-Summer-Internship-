PDF AI Chatbot
==============

A Streamlit web app that lets you upload a PDF and ask questions about its content
using AI. Built with Groq, ChromaDB, and Sentence Transformers.


FEATURES
--------
- Upload any text-based PDF
- Ask questions in natural language
- AI answers based on the PDF content only
- Fast responses using Groq's LLM API
- Vector search for accurate context retrieval


TECH STACK
----------
- Python
- Streamlit              (UI)
- Groq API               (LLM)
- ChromaDB               (Vector store)
- Sentence Transformers  (Embeddings)
- PyPDF                  (PDF text extraction)
- python-dotenv          (Environment variables)


PROJECT STRUCTURE
-----------------
pdf-chatbot/
├── app.py               # Main Streamlit app
├── chatbot.py           # Groq AI logic & ask_pdf function
├── pdf_processor.py     # PDF text extraction
├── vector_store.py      # Embeddings & ChromaDB storage
├── requirements.txt     # Dependencies
├── .env                 # API keys (do NOT share)
├── .gitignore
└── README.txt


SETUP INSTRUCTIONS
------------------

1. Clone the repository
   git clone https://github.com/CrwazzyCupcakes/Gen-ai-Summer-Internship-/tree/main.git
   cd pdf-chatbot

2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Set up environment variables
   Create a .env file in the root folder:
   GROQ_API_KEY=your_groq_api_key_here

   Get your free API key at: https://console.groq.com

5. Run the app
   streamlit run app.py

6. Open your browser
   Go to: http://localhost:8501


USAGE
-----
1. Upload a PDF using the file uploader
2. Wait for "PDF Processed Successfully" message
3. Type your question in the input box
4. The AI will answer based on the PDF content

NOTE: Works best with text-based PDFs (reports, research papers, books, contracts).
Scanned/image PDFs may not work correctly.


EXAMPLE QUESTIONS
-----------------
- "What is this document about?"
- "Summarize the main points"
- "What does it say about [topic]?"
- "List all important dates mentioned"
- "What are the key conclusions?"


AUTHOR
------
Afnan Mohammed
Gen-AI Internship Project