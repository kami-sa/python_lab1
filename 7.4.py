cat = []
str = ''
while str != 'СТОП':
    str = input()
    cat.append(str)
flag = 0;
for i in range (len(cat)):
    cat[i].lower()
    if 'кот' in cat[i]:
        flag = i + 1
        break
if flag != 0:
    print (flag)
else:
    print('-1')