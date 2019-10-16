import math

print('Введите число')
num = int(input())
power = math.log2(num)
if power.is_integer():
    print(int(power))
else:
    print('НЕТ')