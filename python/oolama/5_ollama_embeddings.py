from langchain_community.embeddings import OllamaEmbeddings

embedding = OllamaEmbeddings(model='llama3')

documents = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Kolkata is the cultural capital of India"
]

vector = embedding.embed_documents(documents)

print(str(vector))