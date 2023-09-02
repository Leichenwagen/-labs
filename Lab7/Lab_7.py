# Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
# В программе должны быть реализованы минимум один класс, три атрибута, два метода
# Задание- В филармонии 13 музыкальных инструментов (музыкантов). Отбирая трио с допустимым минимальным уровнем навыка игры
# на инструменте у каждого музыканта и со стоимостью не больше указанного бюджета, найти вариант трио с наибольшей суммой навыка,
# которая будет больше ограничения в три раза с наиболее выгодной стоимостью.
try:
    class Philharmony:
        def __init__(self, instruments):
            self.instruments = instruments #ссылаемся на список инструментов
        def find_best_trio(self, min_skill, max_budget): # Перебираем методом все возможные комбинации трио из объектов
            best_trio = None
            max_sum_skill = 0
            min_cost = float('inf')
            for i in range(len(self.instruments)):
                for j in range(i + 1, len(self.instruments)):
                    for k in range(j + 1, len(self.instruments)):# Проверяем, что все инструменты в трио удовлетворяют условиям
                        trio = [self.instruments[i], self.instruments[j], self.instruments[k]]
                        if all(instrument.skill >= min_skill and instrument.cost <= max_budget for instrument in trio):
                            sum_skill = sum(instrument.skill for instrument in trio)
                            if sum(instrument.cost for instrument in trio) <= max_budget and sum_skill >= 3 * min_skill:
                                if sum_skill > max_sum_skill or (sum_skill == max_sum_skill and sum(instrument.cost for instrument in trio) < min_cost):
                                    best_trio = trio
                                    max_sum_skill = sum_skill
                                    min_cost = sum(instrument.cost for instrument in trio)
            return best_trio #возвращаем в конце лучший вариант
    class Instrument: #класс(шаблон) для описания инструментов с тремя атрибутами(свойствами)
        def __init__(self, name, skill, cost):
            self.name = name
            self.skill = skill
            self.cost = cost
    instruments = [Instrument("Рояль", 4, 20000), Instrument("Виолончель", 5, 40000), # Создаем объекты(экземпляры) инструментов
                    Instrument("Скрипка", 3, 10000), Instrument("Орган", 3, 10000), Instrument("Альт", 2, 5000),
                    Instrument("Гитара", 4, 20000), Instrument("Труба", 5, 40000), Instrument("Пианино", 5, 40000),
                   Instrument("Фагот", 4, 20000), Instrument("Саксофон", 2, 5000), Instrument("Контрабас", 3, 10000),
                   Instrument("Флейта", 3, 10000), Instrument("Бубен", 2, 5000)]
    philharmony = Philharmony(instruments) # Создаем объект класса филармонии и передаем список инструментов
    min_skill = int(input('\nВведите минимальный уровень умения игры на инструменте (от 2 до 5),учитывайте, что:'
                       '\n2 уровень - 5000 рублей''\n3 уровень - 10000 рублей''\n4 уровень - 20000 рублей''\n5 уровень - 40000 рублей\n ----> '))
    while min_skill < 2 or min_skill > 5:  # ошибка, если число не подходит под условие
        min_skill = int(input('\nВведите натуральное число больше 2, но меньше 5:\n'))
    max_budget = int(input('\nВведите максимальный бюджет для найма музыкантов в трио (начиная от 15000 рублей): '))
    while max_budget < 15000:  # ошибка, если число не подходит под указанное условие
        max_budget = int(input('\nВведите натуральное число больше 15000:\n'))
    best_trio = philharmony.find_best_trio(min_skill, max_budget)#используем метод из класса филармонии для поиска трио
    if best_trio:
        print("___ Лучшее трио инструментов ___")
        for instrument in best_trio:
            print(f"Инструмент: {instrument.name}, Уровень навыка: {instrument.skill}, Стоимость: {instrument.cost}")
        total_cost = sum(instrument.cost for instrument in best_trio)
        total_skill = sum(instrument.skill for instrument in best_trio)
        print("\nОбщая стоимость:", total_cost, ", Общая сумма навыков:", total_skill)
    else:
        print("Нет подходящих трио инструментов, удовлетворяющих условиям.")
except ValueError:
    print('\nПерезапустите программу и введите натуральное число.')
