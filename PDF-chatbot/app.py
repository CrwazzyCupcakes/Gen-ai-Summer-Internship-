import streamlit as st

from pdf_processor import (
    extract_text
)

from vector_store import (
    store_pdf,
    retrieve_chunks
)

from chatbot import ask_pdf

st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="📄"
)

st.title(
    "📄 PDF AI Assistant"
)

st.write(
    "Upload a PDF and ask questions."
)

pdf = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if pdf:

    text = extract_text(pdf)

    store_pdf(text)

    st.success(
        "PDF Processed Successfully"
    )

question = st.text_input(
    "Ask a question"
)

if question:

    chunks = retrieve_chunks(
        question
    )

    answer = ask_pdf(
        question,
        chunks
    )

    st.write(answer)