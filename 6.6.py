import math
summa = 0
for i in range(int(input())):
    summa += 1 / (i+1) ** 2
print((math.pi ** 2) / summa)
