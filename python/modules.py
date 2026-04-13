# module -library
import math
# print(math.sqrt(81))
# sqrt=square root 
# print(pow(10,4))
# pow = pow(digit,power )
# time
# import time
# time.sleep(10)
# print("hogya bhai 10 sec")
# import  datetime
# print(datetime.datetime.now())

# exception handling 
# a=int(input("enter a num.."))
# b=int(input("enter a num.."))
# # print(a/b)
# f=[23,23,34]
# try:
#     print(a/b)
#     print(f[3])
# except IndexError as t:
#     print(t)
# except Exception as r:
#     print(r)
# finally:
#     print('alwayys  executed')


# a=int(input("enter a num.."))
# b=int(input("enter a num.."))
# f=[23,23,34]
# try:
#     print(a/b)
# except Exception as r:
#     print(r)
# try:
#     print(f[3])
# except IndexError as t:
#     print(t)

# finally:
#     print('alwayys  executed')


# filter
# def vov(i):
#   vo='aeiouAEIOU'
#   if i in vo:
#     return True
# v=filter(vov,"nikhil dhiman ")
# print(tuple(v))
# a=[2,34,4,7,6]
# b=[3,45,8,9,1]
# # map filter 
# def sums(i): 
#   return  i+2   
# new=map(sums,a)
# new=map(lambda i,j:i+j,a,b)
# print(list(new))





# a=[2,34,4,7,6]
# b=[3,45,8,9,1]
# # map filter 
# def sums(i): 
#   return  i+2
# new=map(sums,a)
# new=map(lambda i,j:i+j,a,b)
# print(tuple(new))


a=[2,34,4,7,6]
w=2
d1={"name":"nikhil",'class':12,'section':'b','pet':'dog'}
# o=map(d1.upper,a)
# print(a)
l1=['kritish','harshit','prince','ronit','krishh']
u=map(str.upper,l1)
print(list(u))



a=[2,34,4,7,6]
u=map(int +2,a)
print(list(a))
