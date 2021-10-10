num5 = int(input("enter a number "))
num6 = int(input("enter a nnumber "))
op = input("enter operator ")
if op == "addition":
    print(int(num5)+int(num6))
elif op == "*":
    print(int(num5)*int(num6))
elif op == "/":
    print(int(num5)/int(num6))
else:
    print("the opertor doesn't exist")
    op = input("enter operator again  ")
    if op == "addition":
        print(int(num5) + int(num6))
    elif op == "*":
        print(int(num5) * int(num6))
    elif op == "/":
        print(int(num5) / int(num6))
    else:
        print("the opertor doesn't exist")
        op = input("enter operator again  ")
        if op == "addition":
            print(int(num5) + int(num6))
        elif op == "*":
            print(int(num5) * int(num6))
        elif op == "/":
            print(int(num5) / int(num6))