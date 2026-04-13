from transformers import pipeline
summa = pipeline("summarization",model="facebook/bart-large-cnn")
a=input("Enter Your Summary")
print(summa(a,max_length=300,min_length=30,do_sample=False))
