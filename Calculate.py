print('Друг за другом введите два дробных числа')
num1 = float(input())
num2 = float(input())
print('Введите знак операции, которую хотите совершить')
operat = input()
op = '+,-,/,*'
if operat not in op or (operat == '/' and num2 == 0):
    print('8888888')
elif operat == '+':
    print (num1+num2)
elif operat == '-':
    print(num1 - num2)
elif operat == '*':
    print (num1*num2)
elif operat == '/':
    print (num1/num2)