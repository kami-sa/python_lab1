import math
digit1 = 0
digit2 = 0
operation = ''
while operation != 'x':
    digit1 = int(input())
    operation = input()
    if operation != '!' and operation != 'x':
        digit2 = int(input())
    if operation == '+':
        print(digit1+digit2)
    elif operation == '-':
        print(digit1-digit2)
    elif operation == '*':
        print(digit1*digit2)
    elif operation == '/':
        print(digit1/digit2)
    elif operation == '%':
        print(digit1%digit2)
    elif operation == '!':
        print(math.factorial(digit1))
    elif operation == 'x':
        print(digit1)
