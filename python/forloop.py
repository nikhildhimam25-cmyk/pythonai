''' creating a month chart according to its month number '''
print("ENTER NUMBER FROM 1 TO 12 To Know its corresponding month")
a=int(input ("enter a number "))
input
if a==1:
    print("january")
elif a==2:
    print("february")
elif a==3:
    print("march")
elif a==4:
    print("april")
elif a==5:
    print("may")
elif a==6:
    print("june")
elif a==7:
    print("july")
elif a==8:
    print("august")
elif a==9:
    print("september")
elif a==10:
    print("october")
elif a==11:
    print("november")
elif a==12:
    print("december")
else : print("invalid number for month range")
'''task 2'''
print("enter two number for comparison")
a1=int(input("enter first number"))
a2=int(input("enter second number"))
print(a1==a2)
if a1==a2: print("both are equal ")
elif a1!=a2 :
 print("they are not equal ")
elif a1>a2:  
    print("a1 is bigger")
elif a2>a1 :
 print("a2 is bigger") 
else : print("")
# x1=int(input("enter 1st number:"))
# x2=int(input("enter second number :"))
s1=input("enter your name :")
s2=input("enter your surname :")
if a1>a2: 
    for i in range(5):
        print(s1)
elif a2>a1:
 for i in range(3):
    print(s2)
 else:a2==a1 
 print("")
'''task 3 '''
print("enter two words to compare them with is and == ")
string1=input("enter first  word :")
string2=input("enter 2nd word :")
print(string1==string2)
print(string1 is string2)
'''task 4'''
print("comparison with is operator")
num1=int(input("enter 1st number "))
num2=int(input("enter 2nd number "))
print(num1 is num2)

'''5th task'''
q1=int(input("enter a number "))
sum=0
for i in range(1,q1):
    sum+=i

print(sum)
  
'''6th task'''
print("EVEN NUMBER WILL PRINT IN THE RANGE YOU WILL ENTER BELOW ")
e1=int(input("enter a number :"))
for i in range(2,e1):
 if i%2==0:
  print("ALL EVEN NUMBERS ARE",i)
'''7TH TASK''' 
print("you will get number in sequence or backwards ")
num=int(input("enter a number: "))
o=input("enter op..(+,-)")
if o=='+':
  for i in range(num):
    print(i,end=" ",sep=",")
elif o=='-':
 for i in range(num,0,-1):
    print(i,end=" ",sep=",")
else:
   print("invalid operator") 

    