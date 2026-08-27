import streamlit as st



from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text


st.title("Career Intelligence System")
st.write("Your AI-powered career analysis platform.")

uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

if uploaded_resume:
    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_resume)

    st.subheader("Extracted Resume Text")
    st.text_area(
        "Resume content",
        resume_text,
        height=400
    )