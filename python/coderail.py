# creating a simple railway booking system
print("WELCOME TO CODERAIL RAILWAY SYSTEM ")
a=input("ENTER YOUR GOOD NAME:")
b=int(input("ENTER YOUR AGE :"))
if b<=6:
   print("free for kids of age of 6 or less")
elif b>=60:
   print("extra 20% For you ")
else:60<b>6 
print("")
c=input("CHOOSE YOUR CLASS: c1,c2,c3 : ")
if c=="c1":
   price1=1500
   travel_class="first class"
elif c=="c2":
    price2=1000
    travel_class="second class"
elif c=="c3":
    price3=500
    travel_class="third class"
else :print("enter a valid class")
m=input("want to include meal in your journey : type  yes / no :")
if m=="yes":
    print("meal included extra 200 ")
elif m=="no": 
 print("thanks for your answer") 
print("YOUR NAME :",a)
print("YOUR AGE :",b)
print("MEAL INCLUDED :",m)
print("your travel class:",c)
if c=="c1":
   x1=(price1)
   print(x1)
elif c=="c2":
   x1=(price2)
   print(x1)
elif c=="c3":
 x1=(price3)
 print(x1)
if m=="yes":
   print("meal added:",x1+200)
else:m=="no" 
print("")
if b<=6:
   print(" This Journey Is Free For You")
elif b>=60:
   e1=(x1*0.8)
   print("discounted price",e1)
else:6<b>60 
print("")



