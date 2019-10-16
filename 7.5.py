cat = []
str = ''
while str != 'СТОП':
    str = input()
    cat.append(str)
flag = 0;
count = 0
for i in range (len(cat)):
    cat[i].lower()
    if 'кот' in cat[i]:
        if flag == 0:
            flag = i + 1
        count += 1
if flag != 0:
    print ('Первое упоминание: ',flag,' строка, количество упоминаний: ',count)
else:
    print('0 -1')