print('Сейчас мы узнаем о вас всё!')
print('Какое ваше любимое время года?')
inp1=input()
inp1=inp1.upper()
if inp1 == 'ЗИМА' or inp1 == 'ВЕСНА' or inp1 == 'ЛЕТО' or inp1 == 'ОСЕНЬ':
    a = 'Какой из предложенных цветов вам нравится больше: красный, синий или желтый?'
    print(a)
    a = a.upper()
    inp2=input()
    inp2 = inp2.upper()
    if inp2 in a:
        a = 'Если вам предложат сейчас прогуляться, то куда вы пойдете: парк, театр, кино, торговый центр?'
        print(a)
        a = a.upper()
        inp3 = input()
        inp3 = inp3.upper()
        if inp3 in a:
            print('Отлично. Вот ваши результаты:')
            if (inp1 == 'ЗИМА') and (inp2 == 'КРАСНЫЙ' ) and (inp3 == 'ПАРК'):
                print('Думаю, вам стоит завести новые знакомства.')
            elif (inp1 == 'ВЕСНА') and (inp2 == 'СИНИЙ' ) and (inp3 == 'ТЕАТР'):
                print('Вы - неунывающий и легкий на подъем человек.')
            elif (inp1 == 'ЛЕТО') and (inp2 == 'ЖЕЛТЫЙ' ) and (inp3 == 'КИНО'):
                print('Лучшее развлечение для вас - посмотреть фильм в хорошей компании под открытым небом, не так ли?')
            elif (inp1 == 'ОСЕНЬ') and (inp2 == 'КРАСНЫЙ') and (inp3 == 'ТОРГОВЫЙ ЦЕНТР'):
                print('Даже коты не так прекрасны, как вы!')
            elif (inp1 == 'ЗИМА') and (inp2 == 'СИНИЙ') and (inp3 == 'ПАРК'):
                print('Еще немного, и вам обязательно повезет')
            elif (inp1 == 'ЛЕТО') and (inp2 == 'ЖЕЛТЫЙ' ) and (inp3 == 'ТЕАТР'):
                print('Люди обращают внимание на вас благодаря вашей доброте')
            else:
                print('Вы обладаете незаурядным умом!')

        else:
            print('Я вам не верю, нам придется попрощаться.')
    else:
        print('Я вам не верю, нам придется попрощаться.')
else:
    print('Я вам не верю, нам придется попрощаться.')
