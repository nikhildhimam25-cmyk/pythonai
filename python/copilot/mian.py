import git
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate





repo_url=st.text_input("Github repolink")
repo_dir = "git_incoming_data"
git.Repo.clone_from(repo_url, repo_dir)



import os
from langchain_core.documents import Document 

VALID_EXTENSIONS = (
    ".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css", ".scss",
    ".dart", ".kt", ".kts", ".java", ".gradle", ".swift", ".m", ".mm",
    ".c", ".cpp", ".cc", ".h", ".hpp", ".rs", ".go", ".rb", ".php",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".sh", ".bash", ".zsh",
    ".ps1", ".sql", ".md", ".txt", ".rst", ".dockerfile", ".gitignore",
)

def load_clean_files(path):
    docs = []

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in [".git", "node_modules", "dist", "build"]]

        for file in files:
            if not file.endswith(VALID_EXTENSIONS):
                continue

            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    docs.append(Document(          # ✅ Document object
                        page_content=content,
                        metadata={"source": filepath}  # ✅ metadata with path
                    ))
            except:
                pass

    return docs




docs = load_clean_files("D:\\nikhil\\python\\copilot\\git_incoming_data")




EXT_MAP = {
    ".py": Language.PYTHON,
    ".js": Language.JS,
    ".jsx": Language.JS,
    ".ts": Language.TS,
    ".tsx": Language.TS,
    ".java": Language.JAVA,
    ".kt": Language.KOTLIN,
    ".kts": Language.KOTLIN,
    ".cpp": Language.CPP,
    ".cc": Language.CPP,
    ".hpp": Language.CPP,
    ".c": Language.C,
    ".h": Language.C,
    ".go": Language.GO,
    ".rs": Language.RUST,
    ".rb": Language.RUBY,
    ".swift": Language.SWIFT,
    ".html": Language.HTML,
    ".sol": Language.SOL,
    ".php": Language.PHP,
    ".scala": Language.SCALA,

}

chunks = []
@st.cache_resource

def load_eve():
 for doc in docs:
     source = doc.metadata["source"]
     ext = Path(source).suffix
 
     # skip non-code files
     if ext not in VALID_EXTENSIONS and Path(source).name not in VALID_EXTENSIONS:
         continue
 
     language = EXT_MAP.get(ext, None)
 
     if language:
         splitter = RecursiveCharacterTextSplitter.from_language(
             language=language,
             chunk_size=1000,
             chunk_overlap=200
         )
     else:
         # generic for yaml, json, css, dart, sql etc
         splitter = RecursiveCharacterTextSplitter(
             chunk_size=1000,
            chunk_overlap=200
        )

     chunks.extend(splitter.split_documents([doc]))




     emb=HuggingFaceEmbeddings(model="BAAI/bge-base-en-v1.5")



     db=FAISS.from_documents(chunks,emb)



     retriever=db.as_retriever(search_type="similarity",search_kwargs={"k":5})



     prompt = PromptTemplate(
    template="""
You are an expert code explainer. You will be given code chunks from a GitHub repository.
Your job is to explain the code clearly and in simple terms.

Use the following context (code chunks) to answer the question.

Context:
{context}

Question: {question}

Instructions:
- Explain what the code does in simple terms
- Mention which file it belongs to
- Explain functions, classes, logic step by step
- If multiple files are involved, explain each one
- If you don't know, just say "Not found in the repository"

Answer:
""",
    input_variables=["context", "question"]
)



     llm=ChatOllama(model="qwen2.5-coder:7b",temperature=0.1)



     rag_chain=({
    "context":retriever,"question":RunnablePassthrough()
     }|prompt|llm|StrOutputParser())

 return rag_chain
rag_chain=load_eve()

query="explain the code "
response=rag_chain.invoke(query)


query="explain the code "
response=rag_chain.invoke(query)