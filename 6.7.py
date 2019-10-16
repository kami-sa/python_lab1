n = int(input())
sum = 0
for i in range(n):
    digit = int(input())
    if i % 2 == 0:
        sum += digit
    else:
        sum -= digit
print(sum)