def nod(a : int, b : int):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def nok(a : int, b : int):
    return a * b / nod(a, b)


num = int(input('Количество дробинок: '))
numerator = []
denominator = []
for i in range(num):
    numerator.append(int(input()))
    denominator.append(int(input()))
d = []
count = 0
d.append(nok(denominator[0], denominator[1]))
while count != num - 2:
    d.append(nok(d[count], denominator[count + 2]))
    count += 1
nok1 = int(d[len(d)-1])
#print('Наименьшее общее кратное:', nok1)
multiply = []
for i in range(num):
    multiply.append(nok1 // denominator[i])
new_num = 0;
for i in range(num):
    numerator[i] *= multiply[i]
    new_num += numerator[i]
    denominator[i] = nok1
den = denominator[0]
delimiter = nod(new_num, den)
new_num /= delimiter
den /= delimiter
print ('Урон: ')
print(int(new_num))
print(int(den))
