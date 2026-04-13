import random
print("lets play rock paper scissor")
print('1..rock')
print('2..paper')
print('3..scissor')
def input_something(p):
   while True:
    op=input(p).strip().lower()
    if op:
       return op
    print("this cant be blank")
def main():
#  with open ('p.txt','a') as c:
 a='rock','paper','scissor'
 j=(random.choice(a))
 op=input_something('enter your choice..')
 if op==j:
   print('computer choice',j)
   print("its Tie")
   with open ('p.txt','a') as c:
    c.write('its tie\n')

 elif op=='rock' and j=='paper':
    print('computer choice',j)
    print('computer won')
    with open ('p.txt','a') as c:
      c.write('computer won\n')
 elif op=='paper' and j=='scissor':
     print('computer choice',j)
     print('computer won')
     with open ('p.txt','a') as c:
      c.write('computer won\n')
 elif op=='scissor' and j=='rock':
      print('computer choice',j)
      print('computer won')
      with open ('p.txt','a') as c:
       c.write('computer won\n')
 elif op=='scissor' and j=='paper':
  print('computer choice',j)
  print('you won')
  with open ('p.txt','a') as c:
   c.write('you won\n')
 elif op=='paper' and j=='rock':
   print('computer choice',j)
   print('you won')
   with open ('p.txt','a') as c:
    c.write('you won\n')
 elif op=='rock' and j=='scissor':
  print('computer choice',j)
  print('you won')
  with open ('p.txt','a') as c:
   c.write('you won\n')
 else:
  print("invalid")  
   
while True:
 main()
#


  

