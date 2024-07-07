import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

api_key = 'your_google_api_key'

genai.configure(api_key=api_key)

# Initialize the GenerativeModel with the model name
model = genai.GenerativeModel('gemini-1.5-pro-latest')

pdfreader = PdfReader('Sumresh_Resume.pdf')

from typing_extensions import Concatenate
# read text from pdf
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content
        
        

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)


genai.configure(api_key=api_key)

# Initialize the GenerativeModel with the model name
model = genai.GenerativeModel('gemini-1.5-pro-latest')

prompt = f"Generate a entire content of my resume in a json format. Here are my details: {texts}"

# Generate response
response = model.generate_content([prompt])

print(response.text)