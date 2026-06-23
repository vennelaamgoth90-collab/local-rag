import streamlit as st
import fitz  # PyMuPDF

st.title("📄 AI Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

pdf_text = ""

if uploaded_file:
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf:
        pdf_text += page.get_text()

    st.success("PDF uploaded successfully!")

question = st.text_input("Ask a question")

if st.button("Submit"):

    if not pdf_text:
        st.warning("Please upload a PDF first.")
    else:
        question_words = question.lower().split()

        sentences = pdf_text.split(".")

        matches = []

        for sentence in sentences:
            if any(word in sentence.lower() for word in question_words):
                matches.append(sentence)

        if matches:
            st.subheader("Answer")
            st.write(" ".join(matches[:3]))
        else:
            st.write("No relevant answer found in the PDF.")
