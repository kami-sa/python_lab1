n = int(input())
count = 0
while n > 1:
    if n % 2 == 0:
        n /= 2
        count +=1
    else:
        n -= 1
        n /= 2
        count += 2
print(count)