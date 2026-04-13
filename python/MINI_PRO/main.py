import streamlit as st
from  rank_bm25 import BM25Okapi
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


loader = PyPDFLoader("D:\\nikhil\\python\\MINI_PRO\\NCERT-Class-12-Biology.pdf")
docs=loader.load()


text_split=RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=300)
document=text_split.split_documents(docs)


def cleanfxn(text):
    return text.encode("utf-8","ignore").decode("utf-8","ignore")


cleandoc=[]
for files in document:
    files.page_content=cleanfxn(files.page_content)
    cleandoc.append(files)


emb= OllamaEmbeddings(model="nomic-embed-text") 
db= FAISS.from_documents(cleandoc, emb)

retriever=db.as_retriever(search_type="similarity",search_kwargs={"k":5})



prompt=ChatPromptTemplate.from_template(
    """
You are an expert research assistant.

Use ONLY the provided context to answer the question.
- Do not use prior knowledge
- If answer is missing, say: "Not found in the document."

Be concise and precise.

Context:
{context}

Question:
{question}

Answer:
"""
)


llm=Ollama(model="mistral:latest",temperature=0.4)

def formatdoc(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain=(
    {"context":retriever|formatdoc,"question":RunnablePassthrough()
     }
           |prompt|llm|StrOutputParser()
           )

st.set_page_config(page_title="model")


st.title("any question related to biology")



query =st.text_input("enter your ouestion")
if query:
    response = rag_chain.invoke(query)
    st.write(response)
