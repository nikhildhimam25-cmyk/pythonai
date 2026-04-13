import streamlit as st

st.set_page_config(page_title="model",page_icon="🤖")




from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.retrievers import BM25Retriever
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser 


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
 

@st.cache_resource
def  load_everything():
     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
     db = FAISS.load_local(
        'D:\\nikhil\\python\\yogacnn\\faiss_index',
        embeddings,
        allow_dangerous_deserialization=True
     )
    


     all_docs = list(db.docstore._dict.values())
     retriever = db.as_retriever(search_kwargs={"k": 3,"fetch_k":25,"lambda_mult":0.75},search_type="mmr")




     prompt = ChatPromptTemplate.from_template(
     """
     You are a legal assistant designed to help non-lawyers understand legal documents.
     
     Use ONLY the provided context to answer the question.
     
     IMPORTANT RULES:
     - Do NOT use prior knowledge outside the context
     - If the answer is not clearly stated, say: "Not found in the document."
     - Explain in simple, plain English (avoid legal jargon)
     - Be accurate and do not guess
     
     YOUR TASK:
     1. Explain what the relevant part of the document means
     2. Highlight any obligations, risks, or important conditions
     3. If applicable, explain what the user is agreeing to
     
     Context:
     {context}
     
     Question:
     {question}
     
     Answer (in simple terms):
     """
     )




     llm2 = ChatOllama(
    model="mistral:latest", 
    temperature=0.4
     )




     rag_chain = (
         {
             "context": retriever | format_docs,
             "question": RunnablePassthrough()
         }
         | prompt 
         | llm2
         | StrOutputParser()
     )
     return rag_chain
rag_chain=load_everything()
query=st.text_input("enter your question")
if query:
  response=rag_chain.invoke(query)
  st.write(response)





