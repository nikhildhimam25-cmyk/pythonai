# from langchain_openai import ChatOpenAI 
from langchain_core.prompts import ChatPromptTemplate 

from langchain_core.output_parsers import StrOutputParser 
from langchain_community.llms import Ollama 
import streamlit as st 
from dotenv import load_dotenv
import os  

load_dotenv()


os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']="true"


prompt= ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assitant, please respond to user queries"),
        ("user","Question: {question}")
    ]
)
st.title("ChatBOT")

llm=Ollama(model="gemma3:1b")
input_text= st.text_input("Enter Question ")
output= StrOutputParser()

chain= prompt|llm|output

if input_text:
    st.write(chain.invoke({"question":input_text}))
    