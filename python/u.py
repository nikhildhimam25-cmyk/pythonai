# l=["ram",'prisha,''nikhil','pratham','cat','dog','him','food','sem','her',]
# print(l)
# l=["ram",'prisha,''nikhil','pratham','cat','dog','him','food','sem','her',]
# n=[h for h in l if len(h)<4]
# print(n)


# h = [i for i in range(1,21)if i%2==0]
# print('even',h)
# h = [i for i in range(1,21)if i%2!=0]
# print('odd',h)

# u=[k for k in range(1,1001)if k%7==0]
# print(u)

# new ='the hardest choices require strongest wills'
# r= sum([1 for t in new if t==" "])
# print(r)
# 
# list=()
# for i in range(1,11):
#     for z in range(1,11):
#       print(i,"x",z,'=',i*z)

# n=[h**2 for h in range(1,11)]
# print(n)



# n=[h for h in range(1,21)if h%2==0]
# print(n)


# l=["ram",'prisha,''nikhil','pratham','cat','dog','him','food','sem','her',]
# h=[n.upper() for n in l]
# print(h)


# l=["ram",'prisha,''nikhil','pratham','cat','dog','him','food','sem','her',]
# h=[k for k in l if k==("a",'i','u','e','o',)]
# print(h)

# k='hey i am thanos'
# j=[f for f in k if f.lower() in 'aeiou']

# print(j)


# h=[n for n in range(1,51) if n%5==0]
# print(h)



# l=["ram",'prisha,''nikhil','pratham','cat','dog','him','food','sem','her',]
# h=[n for n in l if len(n) > 4]
# print(h)


# t=(12,34,4,56,14,6,12,13,5,2,7,9,8,)
# k=[g**3 for g in t ]
# t=tuple(zip(t,k))
# print(t)

# num= [i for i in range(1,51) if i%2==0]
# print('even',num)

# num= [i for i in range(1,51) if i%2!=0]
# print('odd',num)

# pop='maybe forever is not a myth'
# h=[l for l in pop(len(pop))]
# print(h)
                                        
# s={45,4.56,11,'Hello',False, 100,41,11,32,45}
# print("----------------")

# s.clear()
# print(s)
set1= set()
print(type(set1))



s1={12,1,67,89}
s2={True, 34,67,11}

# print(s2.union(s1))

# print(s1.intersection(s2))

# s1.pop()
# s1.pop()
# s1.pop()
# print(s1)
g=9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
b=8656453454534353454354354356565832423758327278657658756834756876745873586348765843687687648764687453454534353454354354356565832423758327278657658756834756876745873586348765843687687648764687453454534353454354354356565832423758327278657658756834756876745873586348765843687687648764687453454534353454354354356565832423758327278657658756834756876745873586348765843687687648764687453454534353454354354356565832423758327278657658756834756876745873586348765843687687648764687453454534353454354354356565832423758327278657658756834756876745873586348765843687
print(g*b)
t=()
print(type(t))
d={}
print(type(d))
s=set()
print(type(s))
l=[]
print(type(l))
new=[{}]
print(type(new))
# if not movie:
#     print("no movies saved")
#   else:
#   #  li()
#    r=input_something("enter movie name...")
#   for i, j in enumerate(movie):
#    print()
#    print(movie[i]["movie"]==r,'movie found')
#   print(movie[i])
import time
# while True:
#   t=time.strftime("%H:%M:%S")
#   print(t)
#   time.sleep(1)
   
p=time.time()
for i in range(1,1000000):
    pass
e=time.time()
t=('time gap..',e-p)
print(t)


a=int(input("enter count down.."))
while True:
    print('time left..',a)
    time.sleep(1)
    a-=1
    if a==0:
        break
    
# while True:
#  a=int(input("enter count down.."))
 
#  if a>0:
#       a1=input("press enter to start..")
#       if a1=="":
#        for i in range(1,a+1):
#         time.sleep(0.1)
#         c=(i+0.01)
#         c+0.1=c
#  else:
#       print('invalid choice') 
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from groq import Groq
import os, shutil, base64

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={"k": 5})

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "running ✅"}

@app.post("/ask")
def ask(request: QueryRequest):
    result = chain.invoke(request.question)
    return {
        "answer": result["result"],
        "sources": [doc.page_content[:200] for doc in result["source_documents"]]
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
    contents = await file.read()
    base64_image = base64.b64encode(contents).decode("utf-8")
    response = groq_client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                    },
                    {
                        "type": "text",
                        "text": "Extract and explain all important text, clauses and key points from this document image in simple language."
                    }
                ]
            }
        ]
    )
    return {"answer": response.choices[0].message.content}