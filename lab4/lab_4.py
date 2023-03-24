# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных
# по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
# Для отладки использовать не случайное заполнение, а целенаправленное.
# Вид матрицы А:  B C
#                 D E
# 2.Формируется матрица F следующим образом: скопировать в нее А и если в С количество положительных
# элементов в четных столбцах, чем количество отрицательных элементов в нечетных столбцах, то поменять
# местами С и В симметрично, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
# После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется
# выражение: A*AT – K * F*A-1, иначе вычисляется выражение (К*A-1 +G-FТ)*K, где G-нижняя треугольная матрица,
# полученная из А.Выводятся по мере формирования А, F и все матричные операции последовательно.
import numpy as np
from matplotlib import pyplot as plt
try:
    k = int(input("Введите число K, являющееся коэффициентом при умножении: "))
    n = int(input("Введите число N, больше 3 которое является размером матрицы: "))
    while n <= 3:
        n = int(input("Введите число больше 3: "))
    np.set_printoptions(linewidth=10000)
    A = np.random.randint(-10, 10, (n, n))
    length = n // 2
    B = np.array(A[:length, :length])
    C = np.array(A[:length, length+n % 2:n])
    E = np.array(A[length+n % 2:n, length+n % 2:n])
    F = A.copy()
    x = np.array(C)
    print("\nМатрица А\n",A)
    print("\nПодматрица С\n",C)
    chet = np.count_nonzero(x[:,1::2] >= 0)
    nechet = np.count_nonzero(x[:,0::2] < 0)
    if chet > nechet:
        print("Положительных элементов в четных столбцах больше чем количество отрицательных  элементов в нечетных столбцах", chet , ">", nechet,"\nменяем С и В симметрично")
        F[:length, length + n % 2:n] = B[:length, ::-1]
        F[:length, :length] = C[:length, ::-1]
    else:
        print("Положительных элементов в четных столбцах меньше чем количество отрицательных  элементов в нечетных столбцах",chet, "<", nechet,"\nменяем С и Е несимметрично")
        F[:length, length+n % 2:n] = E
        F[length + n % 2:n, length + n % 2:n] = C
    print("\nОтформатированная матрица F\n", F)
    try:
        det = np.linalg.det(A)
        trace = np.trace(F) + np.trace(np.rot90(F))
        print("Определитель матрицы А:", int(det), "\nСумма диагональных элементов матрицы F:", trace)
        if det > trace:
            print("Определитель матрицы А больше суммы диагональных элементов матрицы F", int(det), ">", trace,"вычисляем выражение A*A^T-K*F*A^(-1)")
            result = A * A.transpose() - k * F * np.linalg.inv(A)
            print(result)
        else:
            print("Определитель матрицы А меньше суммы диагональных элементов матрицы F", int(det), "<", trace,"вычисляем выражение (K*A^(-1)+G-F^T)*K")
            G = np.tri(n) * A
            result = (k * np.linalg.inv(A) + G - F.transpose()) * k
            print(result)
    except np.linalg.LinAlgError:
        print("Одна из матриц является вырожденной (определитель равен 0), поэтому обратную матрицу найти невозможно.")
    print("\nМатрица, которая используется при построение графиков:\n", A)
    # Использование библиотеки matplotlib
    av = [np.mean(abs(F[i, ::])) for i in range(n)]
    av = int(sum(av))  # сумма средних значений строк (используется при создании третьего графика)
    fig, axs = plt.subplots(2, 2, figsize=(11, 8))
    x = list(range(1, n + 1))
    for j in range(n):
        y = list(F[j, ::])  # обычный график
        axs[0, 0].plot(x, y, ',-', label=f"{j + 1} строка.")
        axs[0, 0].set(title="График с использованием функции plot:", xlabel='Номер элемента в строке',
                      ylabel='Значение элемента')
        axs[0, 0].grid()
        axs[0, 1].bar(x, y, 0.4, label=f"{j + 1} строка.")  # гистограмма
        axs[0, 1].set(title="График с использованием функции bar:", xlabel='Номер элемента в строке',
                      ylabel='Значение элемента')
        if n <= 10:
            axs[0, 1].legend(loc='lower right')
            axs[0, 1].legend(loc='lower right')
    explode = [0] * (n - 1)  # отношение средних значений от каждой строки
    explode.append(0.1)
    sizes = [round(np.mean(abs(F[i, ::])) * 100 / av, 1) for i in range(n)]
    axs[1, 0].set_title("График с ипользованием функции pie:")
    axs[1, 0].pie(sizes, labels=list(range(1, n + 1)), explode=explode, autopct='%1.1f%%', shadow=True)
    def heatmap(data, row_labels, col_labels, ax, cbar_kw={}, **kwargs):  # аннотированная тепловая карта
        im = ax.imshow(data, **kwargs)
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
        ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)
        return im, cbar
    def annotate_heatmap(im, data=None, textcolors=("black", "white"), threshold=0):
        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()
        kw = dict(horizontalalignment="center", verticalalignment="center")
        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(data[i, j] > threshold)])
                text = im.axes.text(j, i, data[i, j], **kw)
                texts.append(text)
        return texts
    im, cbar = heatmap(F, list(range(n)), list(range(n)), ax=axs[1, 1], cmap="magma_r")
    texts = annotate_heatmap(im)
    axs[1, 1].set(title="Создание аннотированных тепловых карт:", xlabel="Номер столбца", ylabel="Номер строки")
    plt.suptitle("Использование библиотеки matplotlib")
    plt.tight_layout()
    plt.show()
except ValueError:
    print("Программа завершена, введите число")