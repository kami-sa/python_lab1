print('Введите ваш логин. В нем не должно быть символа "@": ')
login = input();
print('Введите резервную почту: ')
mail = input();
if "@" in mail and "@" not in login:
    print('OK')
elif "@" in login and "@" in mail:
    print('Некорректный логин.')
elif "@" not in mail and "@" not in login:
    print('Некорректный почтовый адрес.')
else:
    print('Некорректные логин и почтовый адрес.')


