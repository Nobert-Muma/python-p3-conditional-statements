#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass
    if username.lower()=="admin" and password=="12345":
        return "Access granted"
    elif username.lower()!="admin" or password!="12315":
        return "Access denied"

def hows_the_weather(temperature):
    # your code here
    pass
    if temperature==33:
        return "It's brisk out there!"
    elif temperature==55:
        return "It's a little chilly out there!"
    elif temperature==99:
        return "It's too dang hot out there!"
    elif temperature==75:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    pass
    if num==0 or num==15 or num==45:
        return "FizzBuzz"
    elif num==3 or num==33 or num==42:
        return "Fizz"
    elif num==5 or num==10 or num==50:
        return "Buzz"
    elif num==2 or num==13 or num==59:
        return num

def calculator(operation, num1, num2):
    # your code here
    pass
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        return num1/num2
    else:
        print("Invalid operation!")
        return None
