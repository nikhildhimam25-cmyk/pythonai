a=int(input("enter a number :"))
c=(input("enter operator :"))
b=int(input("enter a number :"))
if c=='+':
  print(a+b)
elif c=="-":
   print(a-b)
elif c=="x":
    print(a*b)
elif c=="/":
      print(a/b)
elif c=="":
        print(int(input("enter operator")))
else:
        print("invalid operator")
        print(int(input("enter operator")))
