#Натуральные числа. Менять местами каждые два соседних числа пока не встретится число из 3 подряд идущих нулей.
# После чего менять только каждую третью пару. Последнее число вывести словами.
import re
numbers =''
num2=[]
def slovami(n):        #словарь
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)
fl= open('test.txt', 'r')
# while True:
arr = fl.readline().split()
if not arr:
    print('Файл пуст, выберите другой файл')
else:
    for i in arr:
        numbers=re.findall(r'^\d+$', i)
        num2+=numbers
if not num2:  # если цифры не встретились в файле
    print('Нет подходящих чисел')
else:
    print(num2)
    res=[]
    count=0
    h=True
    for n in range(len(num2)):
        if count!=0:
            count-= 1
            if count== 4:
                try:
                    for p in range(1, 5):
                        res.append(num2[n+p])
                except IndexError:
                    continue
            continue
        if num2[n] == '000':  # смена каждой 3й пары после нулей
            try:
                h = False
                count = 4
                for j in range(1, 5):
                    res.append(num2[n+j])
            except IndexError:
                break
        else:
            if h:
                try:
                    if num2[n + 1] == '000':
                        res.append(num2[n])
                        res.append(num2[n + 1])
                        count = 0
                    else:
                        res.append(num2[n + 1])
                        res.append(num2[n])
                        count = 1
                except IndexError:
                    res.append(num2[n])
                    count = 1
            else:
                try:
                    res.append(num2[n + 1])
                    res.append(num2[n])
                except IndexError:
                    res.append(num2[n])
                count = 5
    print(res)
    s = res[len(res) - 1] + ' -'
    for i in res[len(res) - 1]:
        s += ' ' + slovami(int(i))
    print(s)