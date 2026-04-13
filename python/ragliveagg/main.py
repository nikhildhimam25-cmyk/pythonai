from fastapi import FastAPI,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os,shutil,base64
from langchain_community.document_loaders import PyPDFLoader
from groq import Groq
load_dotenv()
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# db = FAISS.load_local(
#     "D:\\nikhil\\python\\ragliveagg\\faiss_index",
#     embeddings,
#     allow_dangerous_deserialization=True
# )

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("law-ai")
db = PineconeVectorStore(index=index, embedding=embeddings, text_key="text")



retriever = db.as_retriever(search_kwargs={"k": 5})


llm = ChatGroq(
    model="llama-3.1-8b-instant",  
    api_key=os.getenv("GROQ_API_KEY")
)


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


ragchain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

groq_client=Groq(api_key=os.getenv("GROQ_API_KEY"))

class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"status": "Agreement Explainer API running ✅"}


@app.post("/ask")
def ask(request: QueryRequest):
    result = ragchain.invoke(request.question)
    return {
        "question": request.question,
        "answer": result["result"],
        "sources": [
            doc.page_content[:200] 
            for doc in result["source_documents"]
        ]
    }

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    loader = PyPDFLoader(temp_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)
    global db, retriever
    new_db = FAISS.from_documents(chunks, embeddings)
    db.merge_from(new_db)
    db.save_local("faiss_index")
    retriever = db.as_retriever(search_kwargs={"k": 5})
    os.remove(temp_path)
    return {"message": f"{file.filename} added ✅", "chunks": len(chunks)}



@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        content_type = file.content_type
        base64_image = base64.b64encode(contents).decode("utf-8")

        response = groq_client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{content_type};base64,{base64_image}"
                            }
                        },
                        {
                            "type": "text",
                            "text": "Explain this document in simple terms"
                        }
                    ]
                }
            ]
        )

        return {"answer": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}

# @app.post("/upload-image")
# async def upload_image(file: UploadFile = File(...)):
#     contents = await file.read()
#     base64_image = base64.b64encode(contents).decode("utf-8")
#     response = groq_client.chat.completions.create(
#         model="meta-llama/llama-4-scout-17b-16e-instruct",
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "image_url",
#                         "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
#                     },
#                     {
#                         "type": "text",
#                         "text": "Extract and explain all important text, clauses and key points from this document image in simple language."
#                     }
#                 ]
#             }
#         ]
#     )
#     return {"answer": response.choices[0].message.content}