# # functiion defination 

# def add(a,b):
#   print(a+b)
#   return(a+b)



# add(12,3)
# add(23,27) 

# def avg(a,b,c):
#   print(a+b+c/3)
#   return(a+b+c/3)

# avg(12,2,23)



# l1=['jamai raja','kritish','harshit','prince','ronit','krishh']
 

# def l(list):
#   print(len(list))
#   return(len(list))

# l(l1)


# l2=["food",'app','dharampal','adarsh','cute','cut','rat','raj','dj','prisha','nikhil', ]
# def e(list):
#   for i in list:
#     print(i)

# e(l2)
# e(l1)

# def n(a,x):
#     b=1
#     for i in range(1,x+1):
#      b*=i
#     print(b)
    

# n(1,6)


# def tell(a):
#   if a%2==0:
#     return("even")
#   else:
#     return("odd")
  

# c=int(input("enter a number...."))
# print(tell(c))


# def oddeven():
#  a=int(input("enter a num.."))
#  if a%2==0:
#   print("even")
#  else:
#   a%2!=0
#   print("odd")
# oddeven()

# #  fnc with key word agrument
# def fnckey(a=23,b=56,c=66):
#     print(c,a,b)
# fnckey()
    
# def keyfnc(a,b,m):
#     print(a,b,m)

# keyfnc(a=34,b=45,m=23)
#                                     arbitrary arguements
def args(*y):
    for i,n in enumerate(y,start=1):
     print(i,":",n)
args(23)
args(23,76)
args(23,76,98)
args(23,76,98,87)
args(23,76,98,87,34)





# key words arbitrary arguements '''  kwargs '''
# def kwargs(**i):
#     for j,u in enumerate(i.values()):
#       print(u)
#     for j,u in enumerate(i.items()):
#       print(u)
      # for val in i.items():
      #  print(val)
# kwargs (a=23)
# kwargs (a=23,b=98)
# kwargs (a=23,b=98,c=87)
# kwargs (a=23,b=98,c=87,d=65)
# kwargs (a=23,b=98,c=87,d=65,e=45)


# lambda fxn - anoymous fxn ,single line fxn
# variable name =lambdaa  perimeter :statement
# sums= lambda a,b :a+b
# print(sums(23,45))

# add=lambda a=int(input("enter a number..")),b=int(input("enter a number..")):a+b
# print(add())
# oddeven=lambda a=int(input("enter a number..")):"even" if a%2==0 else "odd" # b=int(input("enter a number.."))
# print(oddeven())
# d=[{"name":"nikhil",'class':12,'section':'b','pet':'dog'}, {"name": 'Ford','class':1964, 'section':'Mustang', 'pet': 'red'}]
# a=input("enter movie name..")
# checkin=lambda a=input("enter name.."):"present" if a in d else 'not present'
# print(checkin())
# # if a in (d[i]["name"]):
#  print('NO MOVIES FOUND')

    



# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

# Sample Output:
# 25
# 48
# Click me to see the sample solution

# print(23*23)
# import random
# a='rock','paper','scissor'
# print(random.choice(a))
# xyy=lambda a=int(input("enter a num..")),b=int(input("enter a num..")): (a+15)*b
# print(xyy())





# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
# Click me to see the sample solution

# import random 
# dom=lambda a=int(input("enter a num")):a*2
# print(dom())


# def ed(**i):
#   a1=int(input("enter num.."))
#   b1=int(input("enter num.."))
#   c1=int(input("enter num.."))
#   a=a1
#   b=b1
#   c=c1
#   print(a,b,c)
  
# def op(*t):
#   for i,j in enumerate(range(1,101),start=1):
#    print(i,":",j)
# op()

# def ok(*t):
#   a=range(1,101)
#   for i,j in enumerate(a,start=1):
#    if i%2==0:
#     print(i)
# ok()

# i,":",

# def os(*t):
#  for i in range(1,100) :
#   for j in range(1,i):
#    if i%2==0:
#     print(i,j)
# os()


# u=lambda a=int(input("enter nu..")) :a**2
# print(u())



a=lambda a=int(input("enter nu..")):'even'if a%2==0 else "odd",
print(a())


# a=lambda a=int(input("enter nu..")):a+10
# print(a())


# a=lambda a=input("enter word.."):a[-1]
# print(a())

# a=lambda a=input("enter word..").lower():'true'if a[0]=='a'else 'False'
# print(a())


a=lambda a=int(input("enter a number..")),b=int(input("enter a number..")):a+'a is gretaor' if a>b else 'b is greator'
print(a())
 

# a=[1,2,3,4,5,6,7,8,9,10]
# u=list(map(lambda x:x**2,a))
# print(u)



# functions - two types- user defined, pre-defined functions # print(), input() # def keyword ke saath bnaaye jaate hai - function ke naam ke saath hamesha () aati hai  # def addNum(): #     print('hello class') # addNum() # # def addNum(): # #     a=10 # #     b=30 # #     print(a+b) # # addNum() # def addNumber(a,b): #     print(a+b)     # # ans= addNumber(11,34) # # print(ans) # def addNumRe(a,b): #     print("hello") #     return a+b # print(addNumRe(12,22)) # def oddEven(a): #     if a%2==0: #         return "Even" #     else : #         return "Odd" # i=int(input("Enter number ")) # print(oddEven(i)) # functions -- # functions with keyword arguments # def keyFunc(a,b,c): #     print(a,b,c) # keyFunc(b=11,a=12,c=21) # arbitrary arguments *args def sumss(*i):     # print(i)     s=0     for val in i:         s+=val     print(s)    # sumss(12,23) # sumss(12,23,34) # sumss(12,23,34,56,) # sumss(12,23,3

# def addnum(a,b):
#   return a+b
# addnum(23,45)
# def oddeven():
#  a=int(input("enter a num.."))
#  if a%2==0:
#   print("even")
#  else:
#   # a%2!=0
#   print("odd")
# oddeven()


   



