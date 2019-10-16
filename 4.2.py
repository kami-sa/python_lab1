print('Друг за другом введите значения температуры. Когда захотите закончить, введите число < -300')
num = 0
count = 0
sum = 0
while num > -300:
    num = float(input())
    count+=1
    sum+=num
sum-=num
sum/=(count-1)
print(sum)