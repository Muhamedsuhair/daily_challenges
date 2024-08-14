a=int(input("enter first number\n"))
op=input("enter the operator\n")
b=int(input("enter second number\n"))
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="/":
    print(a/b)
elif op=="*" :
    print(a*b)
else :
    print("invalid operator")
