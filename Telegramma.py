print('Введите сообщение для подсчета стоимости')
text = input()
price = len(text)*40
print(price // 100,'р.', price % 100,' коп.')