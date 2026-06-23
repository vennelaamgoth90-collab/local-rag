import streamlit as st

st.title("📄 AI Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

question = st.text_input("Ask a question")

if st.button("Submit"):
    st.write("Question:", question)
    st.write("Answer: This is a demo deployment on Streamlit Cloud.")
