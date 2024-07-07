import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import google.generativeai as genai

api_key = 'your_google_api_key'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


st.title("Resume Content Generator")
st.markdown("""
    Upload a PDF file of your resume to generate its content in JSON format. 
    This app uses GenerativeAI to analyze and generate text from your resume.
""")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")


if st.button("Generate Resume Content"):
    if uploaded_file is not None:
        # Read PDF file
        pdfreader = PdfReader(uploaded_file)
        raw_text = ''
        for page in pdfreader.pages:
            content = page.extract_text()
            if content:
                raw_text += content


        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)


        prompt = f"Generate the entire content of my resume in JSON format. Here are my details: {texts}"


        response = model.generate_content([prompt])


        st.subheader("Generated Resume Content (JSON format):")
        st.write(response.text)


        st.markdown("""
            <style>
                .stFileUploader label {
                    font-size: 18px;
                }
                .stButton button {
                    background-color: #2ECC71;
                    color: white;
                    font-weight: bold;
                }
                .stTextInput {
                    border: 2px solid #2ECC71;
                    border-radius: 5px;
                    padding: 10px;
                }
                .stMarkdown {
                    font-size: 16px;
                    line-height: 1.6;
                }
            </style>
        """, unsafe_allow_html=True)
