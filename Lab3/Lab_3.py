# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
# B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
# Для тестирования использовать не случайное заполнение, а целенаправленное.
# 2.Формируется матрица F следующим образом: если в С количество положительных элементов
# в четных столбцах в области 2 больше, чем количество отрицательных  элементов в нечетных
# столбцах в области 4, то поменять в С симметрично области 1 и 3 местами, иначе С и Е поменять
# местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:
# (F+A)*AT – K * F. Выводятся по мере формирования А, F и все матричные операции последовательно.
# порядок               2
#   B   C           1       3
#   D   E               4
import random
# функция вывода матрицы
def print_matrix(matrix):
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        k = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{k}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)
    print()
def paste_matrix(matrixF, matrix, index, row_index):
    h = index
    for row in matrix:
        for element in row:
            matrixF[row_index][index] = element
            index += 1
        row_index += 1
        index = h
try:
    print("Введите число K, являющееся коэффициентом при умножении: ")
    k = int(input())
    print("Введите число N, большее или равное 8: ")
    n = int(input())
    print()
    while n < 8:# ошибка, слишком малый порядок матрицы
        n = int(input("Число не подходит по условию, введите число N, большее или равное 8:\n"))
    delit= n // 2
    ser = delit
    if n % 2 != 0:
        ser += 1
# создаем матрицу размером nxn, заполненную случайными числами
    print("Матрица А изначальная:")
    matrixA = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]
# задание матрицы для тестирования
#     matrixA = [[i+j*n for i in range(n)] for j in range(n)]

    # вывод матрицы A
    print_matrix(matrixA)
# резервная копия матрицы A для дальнейших операций
    matrixA_p = [[elem for elem in raw] for raw in matrixA]
# заготовка под транспонированную матрицу A
    matrixA_tr = [[0 for i in range(n)] for j in range(n)]
    print("Матрица A транспонированная:")
# произведение транспонирования матрицы A
    for i in range(n):
        for j in range(n):
            matrixA_tr[i][j] = matrixA_p[j][i]
# вывод транспонированной матрицы A
    print_matrix(matrixA_tr)
# создание матрицы F, на данный момент равной матрице A
    print("Матрица F изначально равная матрице A:")
    matrixF = [[elem for elem in row] for row in matrixA]
    print_matrix(matrixF) # вывод матрицы F
# формируем подматрицу C,
    # порядок подматрицы C, не включая границы
    C = [[0 for i in range(delit)] for j in range(delit)]
    for i in range(delit):
        for j in range(ser, n):
            C[i][j - (ser)] = matrixF[i][j]
    B = [[0 for i in range(delit)] for j in range(delit)]
    for i in range(delit):
        for j in range(delit):
            B[i][j] = matrixF[i][j]
    D = [[0 for i in range(delit)] for j in range(delit)]
    for i in range(delit, n):
        for j in range(delit):
            D[i - (ser)][j] = matrixF[i][j]
    E = [[0 for i in range(delit)] for j in range(delit)]
    for i in range(ser, n):
        for j in range(ser, n):
            E[i - (ser)][j - (ser)] = matrixF[i][j]
    print("Подматрица C матрицы F:")# Выводим подматрицу С
    print_matrix(C)
    obl2_count= 0      # счетчик пол.элементов в области 2 подматрицы С матрицы F
    obl4_count= 0      # счетчик отр.элементов в области 4 подматрицы С матрицы F
    obl2=[]
    obl4=[]
    for i in range(delit):
        for j in range(delit):
            if ((i + j + 1) < delit) and (i < j) and C[i][j] >= 0 and (j+1)%2==0:
                obl2_count+= 1
                obl2.append(C[i][j])
    for i in range(delit):
        for j in range(delit):
            if (i > j) and ((i + j + 1) > ser) and C[i][j] <= 0 and (j+1)%2!=0:
                obl4_count+= 1
                obl4.append(C[i][j])
    print('Положительных элементов в чётных столбцах области 2 => ',obl2_count, obl2)
    print('Отрицательных элементов в нечётных столбцах области 4 => ',obl4_count, obl4)
    matrixF_p = [[elem for elem in row] for row in matrixF] # резервная копия матрицы F для дальнейших операций
    pol=delit-1
    if obl2_count > obl4_count :         # проверка условия
        print("Количество пол.элементов в области 2 больше, чем отриц. элементов в области 4, \n меняем области 1 и 3 симметрично местами.")
        for j in range(0,delit):
            for i in range(0+j,delit-j):
                C[i][j],C[i][pol-j]=C[i][pol-j],C[i][j]
    else:
        print('Количество пол.элементов в области 2 не больше, чем отриц. элементов в области 4, '
              '\n меняем подматрицы C и E местами несимметрично.\nЕсли порядок матрицы нечетный, центральный элемент не меняется.\n')
        C, E = E, C
    print('\nСозданная по условию матрица F:')
    paste_matrix(matrixF, B, 0, 0)
    paste_matrix(matrixF, C, ser, 0)
    paste_matrix(matrixF, E, ser, ser)
    paste_matrix(matrixF, D, 0, ser)
    print_matrix(matrixF)     # выводим уже сформированную матрицу F из подматриц
    print("Результат умножения транспонированной матрицы A на сумму матриц F и A:")
    print("(F+A)")
# заготовка под результат умножения (F+A)*Atr =
    matrixA_umn = [[0 for i in range(n)] for j in range(n)]
# заготовка под результат скобок
    skobki = [[0 for i in range(n)] for j in range(n)]
# производим сумму двух матриц
    for i in range(n):
        for j in range(n):
            skobki[i][j] = matrixA[i][j] + matrixF[i][j]
    print_matrix(skobki)
# производим умножение
    for i in range(n):
        for j in range(n):
            matrixA_umn[i][j] += skobki[i][j] * matrixA_tr[i][j]
    print("(F+A)*Atr = ")
# выводим результат умножения
    print_matrix(matrixA_umn)

    print("Результат умножения матрицы F на коэффициент K:")
    print("K*F =")
# заготовка под результат умножения матрицы F на коэффициент K
    matrixF_umn = [[0 for i in range(n)] for j in range(n)]
# производим умножение матрицы на коэффициент
    for i in range(n):
        for j in range(n):
            matrixF_umn[i][j] = k * matrixF[i][j]
# выводим результат умножения
    print_matrix(matrixF_umn)
    print("Конечный результат (F + A)* Atr - K*F =:")
# заготовка под конечный результат разности
    matrix_res = [[0 for i in range(n)] for j in range(n)]
# производим разность между двумя матрицами
    for i in range(n):
        for j in range(n):
            matrix_res[i][j] = matrixA_umn[i][j] - matrixF_umn[i][j]
# выводим конечный результат работы программы
    print_matrix(matrix_res)
    print("Работа программы завершена.")
except ValueError:# ошибка на случай введения не числа в качестве порядка или коэффициента
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")