print("welcomw to code rail")
a=input("ENTER YOUR GOOD NAME :")
# print(a)
b=int(input("enter your age:"))
# print(b)
c="1...first class 1500 " \
"   2...second class 1000"\
"    3...THIRD  CLASS 500"
print(c)
c1=int(input("CHOOSE YOUR CLAS...1..2..3..."))
m=input("wanted to include meal...yes/no....")
p1=1500
p2=1000
p3=500
print("----TICKET SUMMARY----")
print(a)
print(b)
if c1==1:
    print('FIRST CLASS..')
elif c1==2:
    print("SECOND CLASS..")
else:
    print('THIRD CLASS..')
if m=="yes":
    print("meal included..200  extra")
elif m=="no":
    print('meal excluded')
if b<=5:
    print("THIS JOURNEY IS FREE FOR YOU")
if 5<b<60:
    if c1==1 and m=="yes":
     print(1700)
     if c1==1 and m=="no":
      print(1500)
     if c1==2 and m=="yes":
      print(1200)
      if c1==1 and m=="no":
       print(1000)
       if c1==3 and m=="yes":
        print(700)
        if c1==1 and m=="no":
         print(1700)
if b>60:
   print("discount of 20% ")
   if c1==1 and m=="yes":
     print(1700-(1700*0.20))
     if c1==1 and m=="no":
      print(1500-(1500*0.20))
     if c1==2 and m=="yes":
      print(1200-(1200*0.20))
     if c1==1 and m=="no":
        print(1000-(1000*0.20))
     if c1==3 and m=="yes":
      print(700-(700*0.20))
     if c1==1 and m=="no":
      print(500-(500*0.20))

print("yamraj is with you" 
" Happy journey")

   
