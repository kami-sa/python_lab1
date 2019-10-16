# print('Введите количество камней в куче:')
# a = int(input())
# while a > 0:
#     b = a % 4
#     if b == 0:
#         b = 2
#     print('Забираю камни в количестве', b)
#     a -= b
#     print('Осталось камней:', a)
#     if a == 0:
#         print('Проиграл компьютер!')
#     else:
#         print('Сколько камней вы хотите взять?')
#         b = 0
#         while not (1 <= b <= 3 and b <= a):
#             b = int(input())
#         a -= b
#         print('Осталось камней:', a)
#         if a == 0:
#             print('Вы проиграли!')
from random import *

rocks_count = int(input("Введите количество камней в куче: "))

while rocks_count > 0:
    if rocks_count <= 3:
        rocks_count -= 1
        print('Бот вытянул %d камень. Осталось %d' % (1, rocks_count))

        if rocks_count == 0:
            print('Машинный мир проиграл')
    else:
        turn = randint(1, 3)
        rocks_count -= turn

        print('Бот взял %d камней. Осталось %d.' % (turn, rocks_count))

    your_turn = 0
    while not (1 <= your_turn <= 3 and your_turn <= rocks_count):
        your_turn = int(input("Ваш ход: "))

    rocks_count -= your_turn

    print('Вы взяли %d камней. Осталось %d' % (your_turn, rocks_count))

    if rocks_count == 0:
        print('Вы проиграли!')