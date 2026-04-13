# '''ist task'''
# # find all the words in a string less than 4 characters
# l1=["food",'app','dharampal','adarsh','cute','cut','rat','raj','dj','prisha','nikhil']
# print(l1)

# h=[n for n in l1 if len(n)<4]
# print(h)
# '''2nd task'''
# n=[h for h in range(1,21) if h%2==0 ]
# n.insert(0,"even")
# print(n)
# n=[h for h in range(1,21) if h%2!=0 ]
# n.insert(0,"odd")
# print(n)
# '''3rd task'''
# l=[h for h in range(1,1000)if h%7==0]
# print("number divisible with 7 are",l)
# '''4th task'''
# str1="hello guys how are you i hope you all are fine "
# h=sum([1 for i in str1 if i==" "])
# print(h)
# list_a=[1,2,3,4]
# list_b=[2,3,4,5]
# h=[e for e in list_a if e in list_b ]
# print(h)
# ------------------
# for i in range(1,51):
#     if i%2==0:
#         print(i)

# h=[i for i in range(1,51) if i%2==0]
# print(h)

a=int(input("enter a num ..."))
o=0
for i in range(1,a):  
    o=o+i
print(o)

q1=int(input("enter a number "))
sum=0
for i in range(1,q1):
    sum+=i

print(sum)
h=[i for i in range(1,100) if i%3==0 ]
print(h)