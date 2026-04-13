from langchain_community.llms import Ollama

llm=Ollama(model='llama3')
while True:
    a=input("Enter your query: ")
    if a.lower() in ['exit', 'quit']:
        print("Exiting the bot")
        break
    else:
        result = llm.invoke(a)
        print(result)
