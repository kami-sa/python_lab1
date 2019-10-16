n = int(input('Запас терпения учителя: '))
tact = ['раз', 'два', 'три', 'четыре']
count = -1
while n > 0:
    schet = input()
    count += 1
    ind = count % 4
    if schet != tact[ind]:
        print('Правильных отсчетов было',count,', но теперь вы ошиблись.')
        count = -1
        n -= 1
print('На сегодня хватит.')

