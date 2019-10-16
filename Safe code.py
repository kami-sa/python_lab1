print ('Введите целое трехзначное число')
num = int(input())
if num // 100 > 0 and num // 100 < 10:
    r1 = num % 10
    r2 = (num // 10) % 10
    r3 = num // 100
    if r1 != r2 != r3:
        print('OK')
    else:
        if r1 == r2 == r3:
            print('В числе все цифры одинаковые')
        else:
            print('Две цифры в числе одинаковые')

else:
    print('Число не трехзначное.')