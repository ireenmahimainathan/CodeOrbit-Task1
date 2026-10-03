#simple calculator Task1
def calculator():
    print("*****SIMPLE CALCULATOR*****")
    try:
        num1=float(input("Enter the first number:"))
        op=input("Enter an operator:")
        num2=float(input("Enter the second number:"))

        if op == "+":
            result=num1+num2
        elif op=="-":
            result=num1-num2
        elif op=="*":
            result=num1*num2
        elif op=="/":
            if num2==0:
                print("Error:Cannot divide zero")
                return
            result=num1/num2
        else:
            print("Invalid operator")
            return
        print("Result:",result)
    except ValueError:
        print("Invalid input!!!Please enter numbers only as input")

calculator()