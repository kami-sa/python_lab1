print ('Введите количество камней в 1 и 2 кучах:')
heap1 = int(input('1: '))
heap2 = int(input('2: '))
print('Сначала вводите, из какой кучи хотите забрать камни, а затем - сколько.')
while heap1 > 0 or heap2 > 0:
    where = int(input('Откуда: '))
    how_many = int(input('Сколько: '))
    if where == 1:
        heap1 -= how_many
    elif where == 2:
        heap2 -= how_many
    else:
        print('У нас всего две кучи :(')
    print('Куча 1:', heap1, ' Куча 2: ', heap2)