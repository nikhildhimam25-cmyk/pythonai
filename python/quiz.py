import streamlit as st
print("-------WELCOME TO QUIZ APP---------")
def f(i):
  print(i)
def input_something(p):
   while True:
    op=input(p).strip().lower()
    if op:
       return op
    print("this cant be blank")
def input_int(o):
  while True:
   try: 
    ok=int(input(o))
    if ok>=1 or ok!=int:
         return ok
   except Exception as e:
    f("Invalid enter again..")
def add():
 quizz=[]
 q=input_something("enter question..")
 q1=input_something('1..enter option..')
 q2=input_something('2..enter option..')
 q3=input_something('3..enter option..')
 q4=input_something('4..enter option..')
 while True:
    q5 = input("Enter correct option: ")
    if q5 in q1   or q2 or q3 or q4:
     break
    else:
        print("Invalid answer! Correct option must match one of the choices.")
 quizz.append(q)
 quizz.append(q1)
 quizz.append(q2)
 quizz.append(q3)
 quizz.append(q4)
 quiz.append(quizz)
 ans.append(q5)
 print('Question added sucessfully')
def play():
  if not quiz:
    print("NO QUESTIONS YET")
  else:
   for i,j in enumerate(quiz[0:len(quiz)]):
    print(j)
    a=input_something("Enter your option ")
    if a in ans:
      print(a)
      print("GOOD BACHA")
    else:
      print("wrong answer")
def delete():
  if not quiz:
    print("NO QUESTIONS YET")
  else:
    try:
     s=int(input('enter question number to delete '))-1
     p=quiz.pop(s)
     print('QUESTION DELETED SUCCESSFULLY')
    except Exception as e:
      print('Invalid Enter Again')
def listt():
  if not quiz:
    print("NO QUESTIONS YET")
  else:
    for i,j in enumerate(quiz,start=1):
     print(i,j)
def update():
  if not quiz:
    print("NO QUESTIONS YET")
  a=input_int("enter question number ")-1
  if a>len(quiz):
   print("INVALID QUESTION NUMBER")
  else:
   print("TO CHANGE QUESTION ENTER 0")
   print("TO CHANGE OPTIONS 1/2/3/4") 
   a1=input_int("enter here ")
   a3=input_something("enter new option/question ")
   quiz[a].pop(a1)
   quiz[a].insert(a1,a3)
   print("CHANGE DONE")
quiz=[]
ans=[]
print("--SELECT--")
while True:
 f("--[A]DD A QUIZ--")
 f('--[L]IST OF ALL QUESTIONS--')
 f('--[U]PDATE--')
 f('--[P]LAY QUIZ')
 f('--[D]ELETE QUIZ--')
 f('--[E]XIT--')
 b=len(quiz)
 a=input('ENTER YOUR CHOICE..').lower().strip()
 if a=='a':
   (add())
 elif a=='p':
   (play())
 elif a=='l':
  (listt())
 elif a=='d':
   (delete())
 elif a=='u':
   (update())
 elif a=='e':
  print('GOODBYE BUDDY')
  print('HAVE A MARVELLOUS DAY')
 else:
   print('Invalid Input')