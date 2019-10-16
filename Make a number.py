print ('Введите целое трехзначное число')
num = int(input())
if num // 100 > 0 and num // 100 < 10:
    r1 = num % 10
    r2 = (num // 10) % 10
    r3 = num // 100
    nr1 = r1+r2;
    nr2 = r2+r3;
    if nr1 > nr2:
        print(nr1.__str__()+nr2.__str__())
    else:
        print(nr2.__str__() + nr1.__str__())
else:
    print('Число не трехзначное.')