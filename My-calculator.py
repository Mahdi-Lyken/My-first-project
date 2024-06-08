import math

print("wellcom to my calculater")
for i in range(1000):
    print("+ : sum")
    print("- : sub")
    print("* : mul")
    print("/ : div")
    print("sin")
    print("log")
    print("exit")
    print("please enter your choice :")
    op = input()
    if op == "exit":
        print("thank you my Lord")
        break
    if op == "+" or op == "-" or op == "*" or op == "/":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
    else:
        a = float(input("enter first number: "))


    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            result = "can not divide by zero"
        else:
            result = a / b    
    elif op == "sin":
        result = math.sin(a)
    elif op == "log":
        result = math.log(a)


    print(result)