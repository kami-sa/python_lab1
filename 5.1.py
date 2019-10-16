day = int(input())
month = int(input()) - 2
year = int(input())
if month < 1:
    month += 12
    year -= 1
c = year // 100
year %= 100
nw = (day + ((13 * month - 1) // 5) + year + (year // 4 + c // 4 - 2 * c + 777)) % 7
print(nw)