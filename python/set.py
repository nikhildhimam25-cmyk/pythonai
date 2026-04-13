# a=1
# while a<=10 :
#  print(a)
#  a=(a+1)
'''2'''
# a=2
# while a<=20:
#  print(a)
#  a=a+2
'''3''' 
# a=1
# while a<=20:
#  print(a)
#  a=a+2
'''4'''
# a=int(input("enter any number :"))
# b=1
# while b<=a:
#     print (b)
#     b=b+1
'''5'''
# a=1
# b=0
# while a<=10:
#     b=b+a
#     a=a+1
# print(b)
'''6'''
# n=int(input("enter any number for its table :"))
# a=1
# while a<=10:
#     print('5 x',a,'=',a*n)
#     a=a+1
'''7'''
# a=10
# while a>=1:
#     print(a)
#     a=a-1
'''8'''
# a=int(input("enter a number : "))
# while a!=0:
#     print("enter a valid number to stop this loop")
#     a=int(input('enter :'))
# while a==0:
#  break
# print("loop stopped")
'''9'''
# print square of numbers from 1 to 10 
# a=1
# while a<=10:
#     print(a**2)
#     a=a+1
'''10'''
# print all numbers divisible by 3 from 1 to 30 
# for a in range(1,31):
#  if a%3==0:
#     print(a)
    
'''11'''
# a1=int(input('enter a number : '))
# n=1
# while a1>0:
#     n=(n*a1)
#     a1=a1-1
# print(n) 
# for n in range(101):
# #    if g%4==0]
#  print(n)
# i= '@@@@nikhil dhiman@@@'
# print(i[::-1])
# print(i.count('i'))

# print(i.center(100))
# print(i.index("an"))
# # extend
# li=[23,54,32,100,22,15,19]
# li.extend([676])
# print(li)
# a=(12,45,43,10,47)
# i=(34,)
# print(type(i))

# print(a.index(43))
# print(a.count(43))
# a=(12,45,43,10,47)
# a=list(a)
# a[1]=100
# a=tuple(a)
# print(a)




s={1,2,3,4,5,6,7,8,9,10,34,52,'hello majra'}
print(type(s))
print(s)
s.add(11)
s.discard(5)
print(s)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Find their union, intersection, difference (A - B), and symmetric difference.
print(A.union(B))
print(A.intersection(B))
print(A-B)