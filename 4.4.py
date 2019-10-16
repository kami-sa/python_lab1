print('Введите пароль')
passw = input()
if len(passw) >= 8:
    if '123' not in passw:
        print('Для подтверждения введите пароль еще раз')
        passw1 = input()
        if passw == passw1:
            print('OK')
        else:
            print('Пароли различаются.')
    else:
        print('Простой!')
else:
    print('Короткий!')