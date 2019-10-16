print ('Как Ваши дела?')
answer = input()
answer = answer.upper();
#print(answer)
if ('ХОРОШ' in answer) or ('ПРЕКРАСН' in answer)or ('ОТЛИЧН' in answer):
    print ('Я рада слышать, что у вас всё отлично. Надеюсь, ничего не изменится ;)')
elif ('ПЛОХ' in answer) or ('УЖАСН' in answer):
    print('Мне жаль, но я очень надеюсь, что скоро всё наладится!')
elif (('ХОРОШ' not in answer) and ('ПРЕКРАСН' not in answer) and ('ОТЛИЧН' not in answer)) and (('ПЛОХ' not in answer) and ('УЖАСН' not in answer)) or (' НЕ ' in answer) or ('?' in answer):
    print('Извините, я вас не понимаю. Мне придется уйти')