# print(34+23)
# h="$harry$$$$ nikhil adarsh"
# print(h.split(" "))
# h="$harrydhiman"
# p=h[3:]
# x=p[:-3]
# # print(x)
# import random 
# a='abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ'
# for i in range(3):
#  h=(random.choice(a))
#  print(h)
def INT(ok):
 while True:
  ok=input("enter here").strip().lower()
  if ok:
     yield ok
     print("this can't be blank")
def add():
  q=INT("enter question..")
  q1=INT('1..enter option..')
  q2=INT('2..enter option..')
  q3=INT('3..enter option..')
  q4=INT('4..enter option..')
  q.append