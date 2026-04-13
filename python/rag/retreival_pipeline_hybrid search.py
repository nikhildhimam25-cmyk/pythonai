import os
import numpy as np
from rank_bm25 import BM25Okapi
from langchain_core.prompts import ChatPromptTemplate


from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms import Ollama



def load_vectorstore(path="db/faiss_index"):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return FAISS.load_local(path, embeddings,allow_dangerous_deserialization=True)



def build_bm25(vectorstore):
    print("Building BM25 index")

    docs = vectorstore.similarity_search("", k=1000)

    corpus = [doc.page_content for doc in docs]
    tokenized_corpus = [text.split() for text in corpus]

    bm25 = BM25Okapi(tokenized_corpus)

    return bm25, corpus, docs



def hybrid_retrieve(query, vectorstore, bm25, corpus, docs, k=4):

    vector_results = vectorstore.similarity_search(query, k=k)

    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    top_idx = np.argsort(bm25_scores)[::-1][:k]

    bm25_results = [docs[i] for i in top_idx]

    combined_docs = vector_results + bm25_results

    unique_docs = {doc.page_content: doc for doc in combined_docs}.values()

    return list(unique_docs)[:k]



def generate_answer(query, retrieved_docs):

    llm = Ollama(model="llama3", temperature=0)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         """You are an intelligent AI assistant.

        You MUST follow these rules:
        - Answer ONLY using the provided context.
        - Do NOT make up information.
        - If the answer is not in the context, say: "I don't know".
        - Keep answers clear, structured, and concise.
        - Use bullet points if helpful.
        - If multiple pieces of information are present, summarize them properly.
        """
        ),
        ("user",
         """Context:
{context}

Question:
{query}

Answer:"""
        )
    ])

    # ✅ FIX HERE
    formatted_prompt = prompt.format_messages(
        context=context,
        query=query
    )

    response = llm.invoke(formatted_prompt)

    return response



def rag_pipeline(query):

    print("\nRunning Hybrid RAG Pipeline...\n")

    vectorstore = load_vectorstore()

    bm25, corpus, docs = build_bm25(vectorstore)

    retrieved_docs = hybrid_retrieve(query, vectorstore, bm25, corpus, docs)

    print("Retrieved Contexts:\n")
    for i, doc in enumerate(retrieved_docs):
        print(f"{i+1}. {doc.page_content[:200]}")
        print("-" * 50)

    answer = generate_answer(query, retrieved_docs)

    return answer


if __name__ == "__main__":


    user_query = input("Ask your question: ")

    answer = rag_pipeline(user_query)

    print("\nFINAL ANSWER:\n")
    print(answer)