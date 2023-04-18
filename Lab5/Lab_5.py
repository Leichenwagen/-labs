#Задана рекуррентная функция F(0) = 5; F(1) = 1; F(n) = 2F(n-1) + F(n-2). Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
import matplotlib.pyplot as plt
import timeit
def rek(n): #рекурсивный подход
    if n==0:
        return 5
    elif n==1:
        return 1
    else:
        return 2*rek(n-1)+rek(n-2)
def iter(n): #итеративный подход
    if n == 0:
        return 5
    elif n == 1:
        return 1
    else:
        F_minus_2 = 5
        F_minus_1 = 1
        for i in range(2, n+1):
            F_i = 2 * F_minus_1 + F_minus_2
            F_minus_2,F_minus_1 = F_minus_1,F_i
        return F_i
try:
    n=int(input('\nВведите натуральное число n для функции F(0) = 5; F(1) = 1; F(n) = 2F(n-1) + F(n-2),\nна его основе будет строиться сравнительная таблица:'))
    while n<1: #ошибка, если не натуральные числа
        n=int(input('\nВы ввели не натуральное число. Введите натуральное число:\n'))
    step = int(input('Введите шаг изменения числа для построения таблицы:'))
    while step< 1:
        step= int(input('\nШаг должен быть натуральным числом, введите натуральное число:\n'))
    if n > 100000:
        print('\nРабота программы может занять некоторое время, пожалуйста проявите терпение')
    start =timeit.default_timer()  # счетчик времени и результат работы итерационного подхода
    result = iter(n)
    end = timeit.default_timer()
    print('Результат работы итерационного подхода:', result, '\nВремя работы:', end - start)
    if 40 < n < 100000:
        print('Работа рекурсивного подхода может занять существенное время, подождите')
    start = timeit.default_timer()  # счетчик времени и результат работы рекурсивного подхода
    result = rek(n)
    end =timeit.default_timer()
    print('Результат работы рекурсивного подхода:', result, '\nВремя работы:', end - start)
    if n > 40:
        print('Число n > 40, это может занять время и для получение сравнительной таблицы\n')
    print('Программа формирует сравнительную таблицу и графики времени вычисления рекурсивным и итерационным подходом для n чисел, подождите немного\n')
    rek_times = []  # создание списков для построения таблицы
    rek_values = []
    iter_times = []
    iter_values = []
    n_values = list(range(1, n + 1, step))
    for n in n_values:  # заполнение списков данными
        start = timeit.default_timer()
        rek_values.append(rek(n))
        end = timeit.default_timer()
        rek_times.append(end - start)
        start = timeit.default_timer()
        iter_values.append(iter(n))
        end = timeit.default_timer()
        iter_times.append(end - start)
    table_data = []  # создание и заполнение последующей таблицы
    for i, n in enumerate(n_values):
        table_data.append([n, rek_times[i], iter_times[i], rek_values[i], iter_values[i]])
    print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)','Значение рекурсии', 'Значение итерации'))  # вывод таблицы
    print('-' * 110)
    for data in table_data:
        print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format(data[0], data[1], data[2], data[3], data[4]))
    plt.plot(n_values, rek_times, label='Рекурсия')  # вывод графиков
    plt.plot(n_values, iter_times, label='Итерация')
    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение рекурсивного и итерационного подхода')
    plt.legend()
    plt.show()
    print("\nРабота программы завершена.\n")
except ValueError:
    print('\nПерезапустите программу и введите натуральное число')
except RecursionError:
    print('\nВы превысили глубину рекурсии. Перезапустите программу и введите меньшее число')