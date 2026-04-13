import random
c="1...rock"
d='2...paper'
e='3...scissors'
print(c)
print(d)
print(e)
print('Enter Your Choice ')
a=input("rock,paper,scissor...")
if a!='rock':
 if a!='paper':
   if a!="scissor":
     a=(input("enter a valid choice..."))
     print(a)
l='rock','paper','scissor'
f=(random.choice(l))
print('computer choice',f)
if a==f:
   print("its a tie ")
if a=="rock":
 if f=="scissor":
    print('you won ...rock destroys scisor')
if a=='paper':
 if f=="rock":
  print("you won...paper covers rock")
  if a=='scissor':
    if f=='paper':
      print('you won...scissor cuts paper')
if a=="scissor":
 if f=="rock":
    print('computer won ...rock destroys scisor')
if a=='rock':
 if f=="paper":
  print("computer won...paper covers rock")
  if a=='paper':
    if f=='scissor':
      print('computer won...scissor cuts paper')
    




