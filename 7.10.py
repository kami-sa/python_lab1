price = []
p = -1
while p != 0:
    p = int(input())
    price.append(p)
bought_price = 0
sale_price = 0
flag = 0
for i in range(len(price)-1):
    if price[i] < price[i+1] and flag == 0:
        bought_price = price[i+1]
        flag = 1
    if price[i] > price[i+1] and flag == 1:
        sale_price = price[i+1]
        break
print(bought_price,sale_price,sale_price-bought_price)