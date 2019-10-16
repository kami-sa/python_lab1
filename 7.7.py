n = int(input())
cat = []
for i in range(n):
    cat.append(input())
flag = 0;
for i in range(len(cat)):
    cat[i].lower()
    if 'кот' in cat[i] and flag == 0:
        flag = 1
    if flag == 1 and 'пес' in cat[i]:
        flag = 0
if flag != 0:
    print('МЯУ')
else:
    print('НЕТ')
