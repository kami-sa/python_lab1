# n = int(input())
# cat = []
# for i in range (n):
#     cat.append(input())
# flag = 0;
# for i in range (n):
#     cat[i].lower()
#     if 'кот' in cat[i]:
#         flag = 1
#         break
# if flag == 1:
#     print ('МЯУ')
# else:
#     print('НЕТ')
n = int(input())
cat = []
flag = 0;
for i in range (n):
    cat.append(input())
    cat[i].lower()
    if 'кот' in cat[i]:
        flag = 1
        break
if flag == 1:
    print('МЯУ')
else:
    print('НЕТ')