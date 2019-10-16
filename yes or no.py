array = []
a = ['да', 'нет']
a.sort()
print('Введите два слова: ')
for i in range(2):
    array.append(input())
array.sort()
if array == a or (array[0] == array[1] and (array[0] == 'да' or array[0] == 'нет')):
    print('Верно')
else:
    print('Неверно')

