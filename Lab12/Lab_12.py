''' Вариант 2. Вычислить сумму знакопеременного ряда |х^(2n+1)|/(2n+1)!, где х-матрица ранга к (к и матрица задаются
 случайным образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t
 знаков после запятой. У алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого +.'''
import numpy as np
from decimal import Decimal, getcontext
def count_summ(matrix, t):# Инициализация переменных
    buf_eps = t # Сохранение начальной точности
    t = 1 / (10 ** t)
    print(f'Заданная точность: {t}\n')
    result_matrix = matrix.copy()
    i, fact_n, delta, result_num = 1, 1, 1, 0
    while abs(delta) > t:# Цикл для вычисления суммы ряда, как только добавляемое слагаемое становится меньше т, то выходим из цикла
        n = i * 2 + 1
        fact_n *= (2 * i) * (2 * i + 1) # Вычисление факториала
        result_matrix = np.linalg.matrix_power(matrix, n)# Возведение матрицы в степень n
        matrix_det = Decimal(np.linalg.det(result_matrix))
        delta = matrix_det / Decimal(fact_n)
        result_num += abs(delta) if i == 1 else delta * (-1) ** i  # Добавление слагаемого к сумме ряда
        i += 1
        # print(f'Матрица ({n}-ая степень):\n{result_matrix}')# Вывод информации для отладки
        # print(f'Слагаемое: {delta} \nДетерминант: {matrix_det} \nФакториал {n}: {fact_n} \nТекущая сумма: {result_num}\n')
    print(f"Количество итераций: {i - 1}")
    return result_num
try:# Ввод точности t
    t = int(input("Введите число t, являющееся точностью (количеством знаков после запятой): "))
    while t > 100 or t < 1:# Проверка допустимости введенной точности
        t = int(input("Введите число t, большее или равное 1:\n"))
    k = np.random.randint(2, 10)# Генерация случайной матрицы
    matrix = np.random.uniform(-1, 1, size=(k, k))
    Rang = np.linalg.matrix_rank(matrix)  # Вычисление ранга матрицы x.
    getcontext().prec = t + 100 # Установка точности для десятичных вычислений.
    np.set_printoptions(linewidth=200)
    print(f"Сгенерированная матрица:\n {matrix} \nРанг матрицы: {Rang}")
    summa_tot = count_summ(matrix, t)
    rounded_summa = round(summa_tot, t)
    print(f"Сумма ряда с точностью {t} знаков после запятой с округлением: {rounded_summa}")
except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")
