import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings



def load_documents(docs_path="docs"):
    print(f"Loading documents from: {docs_path}")

    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"Path does not exist: {docs_path}")

    documents = []


    txt_loader = DirectoryLoader(
        docs_path,
        glob="**/*.txt",
        loader_cls=TextLoader, 
        loader_kwargs={"encoding": "utf-8"}
    )
    documents.extend(txt_loader.load())

 
    pdf_loader = DirectoryLoader(
        docs_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
    documents.extend(pdf_loader.load())

    if not documents:
        raise ValueError("No documents found!")

    print(f"Loaded {len(documents)} documents.")
    return documents


def split_documents(documents, chunk_size=800, chunk_overlap=150):
    print("Splitting documents into chunks...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents)


    for chunk in chunks:
        if "source" not in chunk.metadata:
            chunk.metadata["source"] = "unknown"

    print(f" Created {len(chunks)} chunks.")
    return chunks



def create_faiss_index(chunks, persist_directory="db/faiss_index"):
    print("Generating embeddings using Ollama")

    embedding_model = OllamaEmbeddings(
        model="nomic-embed-text"   
    )

    print(" Creating FAISS vector store...")
    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    # Save index
    os.makedirs(persist_directory, exist_ok=True)
    vector_store.save_local(persist_directory)

    print(f"FAISS index saved at: {persist_directory}")



def main():
    docs_path = "docs"

    documents = load_documents(docs_path)
    chunks = split_documents(documents)
    create_faiss_index(chunks)


if __name__ == "__main__":
    main()
