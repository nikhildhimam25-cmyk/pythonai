# import random
# print("lets play rock paper scissor")
# print('1..rock')
# print('2..paper')
# print('3..scissor')
# def input_something(p):
#    while True:
#     op=input(p).strip().lower()
#     if op:
#        return op
#     print("this cant be blank")
# def main():
#  a='rock','paper','scissor'
#  j=(random.choice(a))
#  op=input_something('enter your choice..')
#  if op==j:
#    print('computer choice',j)
#    print("its Tie")
#    if op=='rock' and j=='paper':
#     print('computer choice',j)
#     print('computer won')
#     if op=='paper' and j=='scissor':
#      print('computer choice',j)
#      print('computer won')
#      if op=='scissor' and j=='rock':
#       print('computer choice',j)
#       print('computer won')
#       if op=='scissor' and j=='paper':
#        print('computer choice',j)
#        print('you won')
#        if op=='paper' and j=='rock':
#         print('computer choice',j)
#         print('you won')
#         if op=='rock' and j=='scissor':
#          print('computer choice',j)
#          print('you won')
#  else :
#   print("invalid choice") 
# while True:
#  print('Enter Your Choice ')
#  a=input("rock,paper,scissor...")
#  if a!='rock':
#   if a!='paper':
#     if a!="scissor":
#       a=(input("enter a valid choice..."))
#       print(a)
#  l='rock','paper','scissor'
#  f=(random.choice(l))
#  print('computer choice',f)
#  if a==f:
#     print("its a tie ")
#  if a=="rock"and f=="scissor":
#      print('you won ...rock destroys scisor')
#  if a=='paper'and f=="rock":
#    print("you won...paper covers rock")
#    if a=='scissor'and f=='paper':
#        print('you won...scissor cuts paper')
#  if a=="scissor"and f=="rock":
#      print('computer won ...rock destroys scisor')
#  if a=='rock'and  f=="paper":
#    print("computer won...paper covers rock")
#    if a=='paper'and  f=='scissor':
#        print('computer won...scissor cuts paper')
with open("log.txt", "w") as f:
    print("Hello", file=f)
    print("World", file=f)