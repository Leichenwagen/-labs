#Натуральные числа. Менять местами каждые два соседних числа пока не встретится число из 3 подряд идущих нулей.
# После чего менять только каждую третью пару. Последнее число вывести словами.
num = ['1','2','3','4','5','6','7','8','9','0']
lines = []
numbers = []


def w(n):
    numeros = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return numeros.get(n)


with open('NaL.txt') as f:
    file = f.read()
    for i in file.split():
        lines.append(i)

for i in lines:
    h = 0
    for j in range(len(i)):
        if h > 0:
            h -= 1
            break
        else:
            if i[j] in num:
                number = i[j]
                h = 1
                while True:
                    try:
                        if i[j + h] in num:
                            number += i[j + h]
                        if i[j + h] not in num:
                            break
                        h += 1
                    except IndexError:
                        break
                numbers.append(number)

if len(numbers) == 0:
    print('цифр нет')
    quit()

pod = []
h = True
zag = 0
for i in range(len(numbers)):
    if zag != 0:
        zag -= 1
        if zag == 4:
            try:
                for j in range(1, 5):
                    pod.append(numbers[i + j])
            except IndexError:
                continue
        continue
    if numbers[i] == '000':
        h = False
        zag = 4
        for j in range(1, 5):
            pod.append(numbers[i + j])
    else:
        if h:
            try:
                if numbers[i + 1] == '000':
                    pod.append(numbers[i])
                    pod.append(numbers[i + 1])
                    zag = 0
                else:
                    pod.append(numbers[i + 1])
                    pod.append(numbers[i])
                    zag = 1
            except IndexError:
                pod.append(numbers[i])
                zag = 1
        else:
            try:
                pod.append(numbers[i + 1])
                pod.append(numbers[i])
            except IndexError:
                pod.append(numbers[i])
            zag = 5


s = pod[len(pod) - 1] + '-'
for i in pod[len(pod) - 1]:
    s += ' ' + w(int(i))

print(s)