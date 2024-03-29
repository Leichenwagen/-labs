# Задание - вариант 2.1 часть – В филармонии К музыкальных инструментов (музыкантов). Сформировать все возможные варианты трио
#2 часть – Отбирая трио с допустимым минимальным уровнем навыка игры на инструменте и со стоимостью не больше указанного бюджета,
#          найти вариант трио с наибольшей суммой навыка, который будет больше ограничения в три раза с найменьшими затратами.
instruments = ["балалайка", "рояль", "виолончель", "варган", "скрипка", "альт", "мандолина", "гитара","тарелки", "труба", "тромбон", "пианино",
               "гобой", "арфа", "треугольник", "валторна","кларнет", "фагот", "флейта", "саксофон","гармонь", "лютня", "челеста", "аккордеон",
               "барабаны", "баян", "флейта Пана", "контрабас", "кастаньеты", "ксилофон", "бубен", "орган", "клавесин"]
# Задаем минимальный уровень умения игры на каждом инструменте
min_skill_levels = {"балалайка": 2, "рояль": 4, "виолончель": 5, "варган": 2, "скрипка": 3, "альт": 3, "мандолина": 2,"гитара": 4, "тарелки": 2, "труба": 3,"тромбон": 3,
                    "пианино": 5, "гобой": 2, "арфа": 2, "треугольник": 3, "валторна": 2, "кларнет":2, "фагот": 4, "флейта": 3, "саксофон": 2,"гармонь": 4, "лютня": 3,
                    "челеста": 2, "аккордеон": 3,"барабаны": 2, "баян": 2, "флейта Пана": 2, "контрабас": 3,"кастаньеты": 3, "ксилофон": 3, "бубен": 2, "орган": 3, "клавесин": 5}
costs_dict = {2: 5000, 3: 10000, 4: 20000, 5: 40000} # Задаем цены на найм музыкантов в зависимости от их уровня умения
def sort_key(trio):# Возвращает кортеж из двух значений: суммы умений в трех инструментах и суммарной стоимости найма музыкантов на три инструмента
    return (trio[2], trio[1])
try:
    n = int(input('\nВведите из какого количества Вы хотели бы увидеть варианты трио музыкальных инструментов.' 
                  '\nУчтите, что филармония в своём распоряжении имеет 33 различных инструмента.\n'))
    while n < 4 or n > 33:  # ошибка, если число не подходит под указанное условие
        n = int(input('\nВведите натуральное число больше 3, но меньше 33:\n'))
    trios = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                trio = (instruments[i], instruments[j], instruments[k])
                trios.append(trio)
    print(f'Всего может быть составлено {len(trios)} вариантов трио из {n} музыкантов.\n\n'
          f'Список комбинаций трио из инструментов ({", ".join(instruments[:n])}):\n')
    for count, trio in enumerate(trios, start=1):
        print(f'{count}. {" - ".join(trio)}')
    print('\nНайдём лучший вариант для концерта с ограниченным бюджетом')
    skill = int(input('\nВведите минимальный уровень умения игры на инструменте (от 2 до 5),учитывайте, что:'
                      '\n2 уровень - 5000 рублей''\n3 уровень - 10000 рублей''\n4 уровень - 20000 рублей''\n5 уровень - 40000 рублей\n'))
    while skill < 2 or skill > 5:  # ошибка, если число не подходит под указанное условие
        skill = int(input('\nВведите натуральное число больше 2, но меньше 5:\n'))
    budget = int(input('\nВведите максимальный бюджет для найма музыкантов в трио (начиная от 15000 рублей): '))
    while budget < 15000:  # ошибка, если число не подходит под указанное условие
        budget = int(input('\nВведите натуральное число больше 15000:\n'))
    good_trios = []
    for i in range(n):  # генерация трио сумма навыка которого больше минимума в три раза и которое по тратам не выше бюджета
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                trio = [instruments[i], instruments[j], instruments[k]]
                skill_sum = sum([min_skill_levels[instrument] for instrument in trio])
                cost = sum([costs_dict[min_skill_levels[instrument]] for instrument in trio])
                if (skill_sum >= 3 * skill and cost <= budget):
                    good_trios.append((trio, cost, skill_sum))
    if good_trios:
        good_trios.sort(key=sort_key)  # сортировка по сумме умений и сумме цен
        best_trio = ' - '.join(good_trios[-1][0])
        total_skill = good_trios[-1][2]
        total_cost = good_trios[-1][1]
        print(f'Мы нашли {len(good_trios)} подходящих комбинаций инструментов, ' f'которые удовлетворяют вашим требованиям.\n' 
              f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
              f'Общая сумма умений всех музыкантов в этой комбинации: {total_skill} баллов.')
        bol = int(input("Нужны все варианты? (да - введите 1, нет - введите 0): "))
        if bol == 1:
            print(f"Список остальных комбинаций трио в которых сумма умений больше в три раза минимального уровня игры музыканта (был задан {skill}):")
            for i, trio in enumerate(good_trios, start=1):
                print(f"{i}. {' - '.join(trio[0])}. Общая стоимость: {trio[1]} рублей, " f"сумма умений: {trio[2]} баллов.")
        else:
            print("Спасибо за использование программы!")
    else:
        print('К сожалению, нам не удалось найти комбинацию, которая удовлетворяет вашим требованиям.')
    print('\nРабота программы завершена.\n')
except ValueError:
    print('\nПерезапустите программу и введите натуральное число.')
