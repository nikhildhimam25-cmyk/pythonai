from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.1,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

while True:
    a=input("Enter your query: ")
    if a.lower() in ['exit', 'quit']:
        print("Exiting the bot")
        break
    else:
        result = model.invoke(a)
        print(result.content)
 
