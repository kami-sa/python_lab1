print ('Введите количество камней в 1, 2 и 3 кучах:')
heap1 = int(input('1: '))
heap2 = int(input('2: '))
heap3 = int(input('3: '))
print('Сначала вводите, из какой кучи хотите забрать камни, а затем - сколько.')
while heap1 > 0 or heap2 > 0 or heap3 > 0:
    where = int(input('Откуда: '))
    how_many = int(input('Сколько: '))
    if where == 1:
        heap1 -= how_many
    elif where == 2:
        heap2 -= how_many
    elif where == 3:
        heap3 -= how_many
    else:
        print('У нас всего три кучи :(')
    print('Куча 1:', heap1, ' Куча 2: ', heap2, ' Куча 3: ', heap3)