from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(repo_id="pszemraj/led-large-book-summary",task="text_generation")
model=ChatHuggingFace(llm=llm)
a=input("enter here")
result=model.invoke(a)
print(result.content)