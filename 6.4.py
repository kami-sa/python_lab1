num = int(input('Введите количество подопытных: '))
s = 0
avg = 0
for i in range(num):
    iq = int(input())
    s += iq
    avg = s // (i+1)
    if iq > avg:
        print('>')
    elif iq < avg:
        print('<')
    else:
        print('0')