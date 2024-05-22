def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def divide(a, b):
    return a/b

def multiply(a, b):
    return a*b


x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

choice = int(input("\nEnter your choice from below:\n1) Add \n2) Subtract \n3) Divide \n4)Multiply\n"))


print("Ans is: \n")
if choice==1:
    print(add(x,y))
    
elif choice==2:
    print(sub(x,y))

elif choice==3:
    print(divide(x,y))

elif choice==4:
    print(multiply(x,y))

else:
    print("Enter Valid Choice")