print("WELCOME TO BURGER KING ")
print('------MENU------')
print("item listed below")
a= "a.whooper burger  ₹ 150 "
price1=150
b= "b.crispy veg  ₹ 100"
price2=100
c= "c.chicken wings  ₹ 120"
price3=120
print(a)
print(b)
print(c)
meal=input("choose your happy meal .. 1/2/3...")
if meal=="1":
    print(a)
elif meal=="2":
    print(b)
elif meal=="3":
    print(c)
else:
    print("choose a valid option")
print("choose quantity")
q=int(input("quantity..."))
print("total price")
if meal=="1":
    p1=(price1*q)
    print(p1)
elif meal=="2":
    p1=(price2*q)
    print(p1)
elif meal=="3":
 p1=(price3*q) 
 print(p1)
else:print("")
# coupon code 
print("available coupon ")
print("king50")
print("bk20")
x=(input("enter coupon code if any... "))
if x=="king50":
    print("50%  Discount") 
    final_cost= ("total charge",p1/2)
    print(final_cost)
elif x=="bk20": 
    print("₹20 off")
    final_cost=("total charge",p1-20)
    print(final_cost)
else: 
 print("no coupon detected " \
"total cost",p1)

# print("final_cost",final_cost)
