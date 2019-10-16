a1, a2 = 1, 1000
sign = ''
print('Загадайте число от 1 до 1000')
while sign != '=':
    c = (a1 + a2) // 2
    print(c, '?')
    sign = input()
    if sign == '>':
        a1 = c
    elif sign == '<':
        a2 = c
    elif sign == '=':
        print('Угадали')