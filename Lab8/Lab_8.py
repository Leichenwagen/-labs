#Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации
# (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую
# библиотеку питона.  Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
# В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
class PhilharmonyGUI: #класс для гип с двумя окнами, метод поиска и метод вывода окна, в начале указаны виджеты первого окна
    def __init__(self, instruments):
        self.instruments = instruments
        self.window = tk.Tk()
        self.window.title('Форма для расчёта лучшего трио')

        self.window.geometry('490x470')
        self.window.resizable(False, False)
        custom_font = font.Font(family="Helvetica", size=12)
        self.window.option_add("*Font", custom_font)
        self.frame = tk.Frame(self.window, width=420, height=610)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.canvas=tk.Canvas(self.frame, width=30, height=40)
        self.canvas.place(relx=0.5, rely=0.18, anchor=tk.CENTER)
        self.zadacha_text=tk.Label(self.frame, width=45, height=8, bg='#87DFD6', text='Найдите выгодное трио музыкантов \nдля концерта, указав желательный уровень \nнавыка и максимальный бюджет.'
                                                                           '\n Программа подберёт вариант с меньшей \nстоимостью  и  с наибольшей суммой навыка, \nкоторая  будет больше ограничения в три раза .')
        self.zadacha_text.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        self.min_skill_label = tk.Label(self.frame, width=35, height=3, text="Введите минимальный уровень\n умения игры на инструменте (от 2 до 5):")
        self.min_skill_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.min_skill_entry = tk.Entry(self.frame, width=17, bg='#87DFD6', justify='center')
        self.min_skill_entry.place(relx=0.5, rely=0.52, anchor=tk.CENTER)
        self.max_budget_label = tk.Label(self.frame, width=35, height=3, text="Введите максимальный бюджет \nдля найма музыкантов в трио \n(начиная от 15000 рублей): ")
        self.max_budget_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.max_budget_entry = tk.Entry(self.frame, width=17, bg='#87DFD6', justify='center')
        self.max_budget_entry.place(relx=0.5, rely=0.68, anchor=tk.CENTER)
        self.find_button = tk.Button(self.frame, width=55, height=3, text="Найти трио", command=self.find_best_trio, bd = 1, bg = '#87DFD6',underline = 0 , activebackground = '#2F9296', activeforeground = '#DFF5F2', cursor = 'hand2')
        self.find_button.config(font=('Helvetica', 14))
        self.find_button.place(relx=0.5, rely=0.78, anchor=tk.CENTER)
    def find_best_trio(self):
        try:
            min_skill = int(self.min_skill_entry.get())
            if min_skill < 2 or min_skill > 5:  # ошибка, если число не подходит под условие
                messagebox.showerror("Некорректное число", "Введите натуральное число больше 2, но меньше 5")
                return #зацикливаем ради верного ответа
            max_budget = int(self.max_budget_entry.get())
            if max_budget < 15000:  # ошибка, если число не подходит под указанное условие
                messagebox.showerror("Некорректное число", "Введите натуральное число больше 15000")
                return
            best_trio = None #формирование трио с указанными данными
            max_sum_skill = 0
            min_cost = float('inf')
            for i in range(len(self.instruments)):
                for j in range(i + 1, len(self.instruments)):
                    for k in range(j + 1, len(self.instruments)):
                        trio = [self.instruments[i], self.instruments[j], self.instruments[k]]
                        if all(instrument.skill >= min_skill and instrument.cost <= max_budget for instrument in trio):
                            sum_skill = sum(instrument.skill for instrument in trio)
                            if sum(instrument.cost for instrument in trio) <= max_budget and sum_skill >= 3 * min_skill:
                                if sum_skill > max_sum_skill or (sum_skill == max_sum_skill and sum(instrument.cost for instrument in trio) < min_cost):
                                    best_trio = trio
                                    max_sum_skill = sum_skill
                                    min_cost = sum(instrument.cost for instrument in trio)
            if best_trio: #вывод результата поиска
                self.results_window = tk.Tk()#открытие окна с результатом
                self.results_window.title('Полученный результат')
                self.results_window['bg'] = '#2F9296'
                self.results_window.geometry('550x400')
                self.results_window.resizable(False, False)
                self.results_label = tk.Label(self.results_window, width=55, height=10, text="", bg='#87DFD6')
                self.results_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                self.results_label.config(font=('Helvetica',12))
                result_text = " Лучшее трио инструментов\n"
                for instrument in best_trio:
                    result_text +=f"Инструмент: {instrument.name}, Уровень навыка: {instrument.skill}, Стоимость: {instrument.cost}\n"
                total_cost = sum(instrument.cost for instrument in best_trio)
                total_skill = sum(instrument.skill for instrument in best_trio)
                result_text += f"\nОбщая стоимость: {total_cost},\n Общая сумма навыков: {total_skill}"
                self.results_label.config(text=result_text)
            else:
                messagebox.showerror("Результат", "Нет подходящих трио инструментов, удовлетворяющих условиям.")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите натуральные числа!")
    def start(self):
        self.window.mainloop()
class Instrument: #класс для инструментов
    def __init__(self, name, skill, cost):
        self.name = name
        self.skill = skill
        self.cost = cost
def main():#функция передающая список объектов классу гип и запускающая метод гип
    instruments=[Instrument("Рояль", 4, 20000), Instrument("Виолончель", 5, 40000), # Список из созданных объектов(экземпляров) инструментов
                    Instrument("Скрипка", 3, 10000), Instrument("Орган", 3, 10000), Instrument("Альт", 2, 5000),
                    Instrument("Гитара", 4, 20000), Instrument("Труба", 5, 40000), Instrument("Пианино", 5, 40000),
                   Instrument("Фагот", 4, 20000), Instrument("Саксофон", 2, 5000), Instrument("Контрабас", 3, 10000),
                   Instrument("Флейта", 3, 10000), Instrument("Бубен", 2, 5000)]
    philharmony_gui = PhilharmonyGUI(instruments)
    philharmony_gui.start()
if __name__ == "__main__":#только при запуске напрямую
