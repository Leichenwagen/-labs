#Натуральные числа. Менять местами каждые два соседних числа пока не встретится число из 3 подряд идущих нулей.
# После чего менять только каждую третью пару. Последнее число вывести словами.
buffer_len = 1   #размер буфера
work_buffer = '' #рабочий буфер
numbers = []
def slovami(n):        #словарь
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)
with open('test.txt', 'r') as f:   #открытие и чтение файла поблочно
    buffer = f.read(buffer_len)
    if not buffer:
        print('Файл пуст, выберите другой файл')
    while buffer:
        while '0' <= buffer <= '9':     #проверка на цифру
            work_buffer += buffer       #добавление цифры к числу последовтельности
            buffer = f.read(buffer_len) #прочтение следущих символов
        if len(work_buffer) > 0:        #если длина рабочего буфера больше нуля, добавить в список
            numbers.append(work_buffer)
        work_buffer = ''
        buffer = f.read(buffer_len)
    if not numbers:       #если цифры не встретились в файле
        print('Нет подходящих чисел')
    else:
        print(numbers)   #вывод последовательности чисел
        answer = []
        h = True
        zag = 0          #счётчик для перемещения пар чисел
        for i in range(len(numbers)):
            if zag != 0:
                zag -= 1
                if zag == 4:
                    try:
                        for j in range(1, 5):
                            answer.append(numbers[i + j])
                    except IndexError:
                        continue
                continue
            if numbers[i] == '000':       #смена каждой 3й пары после нулей
                h = False
                zag = 4
                for j in range(0, 5):
                    answer.append(numbers[i + j])
            else:
                if h:
                    try:
                        if numbers[i + 1] == '000':
                            answer.append(numbers[i])
                            answer.append(numbers[i + 1])
                            zag = 0
                        else:
                            answer.append(numbers[i + 1])
                            answer.append(numbers[i])
                            zag = 1
                    except IndexError:
                        answer.append(numbers[i])
                        zag = 1
                else:
                    try:
                        answer.append(numbers[i + 1])
                        answer.append(numbers[i])
                    except IndexError:
                        answer.append(numbers[i])
                    zag = 5
        print(answer)
        s = answer[len(answer) - 1] + ' -'
        for i in answer[len(answer) - 1]:
            s += ' ' + slovami(int(i))
        print(s)