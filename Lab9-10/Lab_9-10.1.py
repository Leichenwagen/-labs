import tkinter as tk
from tkinter import ttk, messagebox as mb
import os
from idlelib.tooltip import Hovertip

class LoginWindow: #окошко входа\регистрации
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Вход/Регистрация")
        self.window.geometry('550x560')
        self.window.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Bahnschrift', 18), padding=10)
        self.style.configure('Btt.TButton', font= ('Bahnschrift bold', 14), width=25, padding=7)

        self.testL = ttk.Label(self.window, text='ВХОД').place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.testL = ttk.Label(self.window, text='для подсказки наведите курсор на поле ввода', font=('Bahnschrift', 12)).place(relx=0.5, rely=0.22, anchor=tk.CENTER)
        self.login_label = ttk.Label(self.window, text="👤Логин:").place(relx=0.28, rely=0.4, anchor=tk.CENTER)
        self.login_entry = ttk.Entry(self.window)
        self.login_entry.config(validate='key', validatecommand=(self.window.register(self.validate_length), "%P"), font= 'Bahnschrift 14', width=12)
        self.login_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.password_label = ttk.Label(self.window, text="🔑Пароль:").place(relx=0.27, rely=0.5, anchor=tk.CENTER)
        self.password_entry = ttk.Entry(self.window, show='*')
        self.password_entry.config(validate='key', validatecommand=(self.window.register(self.validate_length), "%P"), font= 'Bahnschrift 14', width=12)
        self.password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.toggle_password_button = ttk.Button(self.window, text='Показать пароль', command=self.show_password, cursor='hand2')
        self.toggle_password_button.place(relx=0.71, rely=0.5, anchor=tk.CENTER)
        self.login_button = ttk.Button(self.window, text="Вход", command=self.login,  cursor='hand2', style='Btt.TButton')
        self.login_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        self.register_button = ttk.Button(self.window, width=25, text="Зарегистрироваться", command=self.register,  cursor='hand2', style='Btt.TButton')
        self.register_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.TipLogin = Hovertip(self.login_entry,'Логин должен быть более 5 символов \n и содержать хотя бы одну цифру, \n макс. длина - 10 символов')
        self.TipPassword = Hovertip(self.password_entry,'Пароль должен быть более 7 символов \n и содержать хотя бы одну цифру и одну букву, \n макс. длина - 10 символов')

        if not os.path.exists('DataFile.json'): #создание нового файла при отсутствии
            with open('DataFile.json', 'w'): pass
    def login(self): #обработка входа
        login = self.login_entry.get()
        password = self.password_entry.get()
        if not login or not password:
            mb.showerror("Авторизация", "Пожалуйста, заполните все поля")
            return

        with open("DataFile.json", "r") as file: #чтение файла на присутствие вводимых данных
            lines = file.readlines()
            user_found = False
            incorrect_password = False
            for line in lines:
                stored_name, stored_username, stored_password = line.strip().split('•')
                if login == stored_username:
                    if password == stored_password:
                        user_found = True
                        name = stored_name
                        self.open_account_window(name)
                        break
                    else:
                        incorrect_password = True
                        break
            if not user_found or incorrect_password:
                mb.showerror("Вход", "Неверный логин или пароль")
            return
    def register(self): #изменение окна под регистрацию
        self.register_button.destroy()
        self.name_label = ttk.Label(self.window, text="🖌Имя:").place(relx=0.3, rely=0.3, anchor=tk.CENTER)
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.config(validate='key', validatecommand=(self.window.register(self.validate_length), "%P"), font= 'Bahnschrift 14', width=12)
        self.name_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.TipName = Hovertip(self.name_entry,'Имя должно быть длиною не менее 2 символов, \nно не более 10 символов')
        self.reg_button = ttk.Button(text="Зарегистрироваться", command=self.add_user, cursor = 'hand2', style='Btt.TButton').place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.textL2 = ttk.Label(self.window, text='РЕГИСТРАЦИЯ').place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    def validate_length(self, text):#ограничение на ввод до десяти символов
        if len(text) <= 10:
            return True
        else:
            return False
    def add_user(self):#добавление нового пользователя и проверка вводимых данных
        name = self.name_entry.get()
        login = self.login_entry.get()
        password = self.password_entry.get()
        if not name or not login or not password:
            mb.showwarning('Регистрация', 'Пожалуйста заполните все поля')
            return
        else: #ограничения на ввод данных
            if (len(name) < 2) or (len(login) < 5) or (len(password) < 7):
                mb.showwarning('Ошибка регистрации', 'Проверьте количество символов, возможно оно меньше допустимого.')
                return
            elif not any(char.isdigit() for char in login):
                mb.showwarning('Ошибка регистрации', 'Логин должен содержать хотя бы одну цифру.')
                return
            elif not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                mb.showwarning('Ошибка регистрации', 'Пароль должен содержать хотя бы одну цифру и одну букву.')
                return

        with open("DataFile.json", "r") as file: #чтение файла на поиск схожего
            lines = file.readlines()
            for line in lines:
                _, stored_login, _ = line.strip().split('•') #игнорируем в поиске всё кроме логина
                if login == stored_login:
                    mb.showwarning("Регистрация", "Пользователь с таким именем уже существует")
                    return
        with open('DataFile.json', 'a') as file: #запись пользователя в файлик через точку
            file.write(f'{name}•{login}•{password}\n')
            mb.showinfo('Успешная регистрация', 'Вы успешно зарегистрировались!')
            self.open_account_window(name)
    def open_account_window(self, name): #открытие окна после входа
        self.account_window = tk.Tk()
        self.account_window.geometry('450x360')
        self.account_window.resizable(False,False)
        self.account_window.title("Личный кабинет")
        self.window.destroy()
        self.info_label = ttk.Label(self.account_window,font=('Bahnschrift', 18), text="Добро пожаловать, {}!" .format(name)).place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        self.info_label_mini = ttk.Label(self.account_window, font=('Bahnschrift', 10),text="Вы можете сыграть \nв крестики-нолики с компьютером").place(relx=0.5, rely=0.45,anchor=tk.CENTER)
        self.logout_button = ttk.Button(self.account_window, text="НАЧАТЬ ИГРУ", command=self.logout, cursor='hand2', width=25).place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    def logout(self): #для выхода из программы
        self.account_window.destroy()
        self.board1 = TicTacToe()
        self.board1.window_board()
    def show_password(self): #для скрытие\показа пароля
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
            self.toggle_password_button.config(text="Скрыть пароль")
        else:
            self.password_entry.config(show="*")
            self.toggle_password_button.config(text="Показать пароль")
    def start(self):
        self.window.mainloop()

class TicTacToe: #окошко с игрой
    def __init__(self):
        pass
    def window_board(self):
        self.game_window = tk.Tk()
        self.game_window.geometry('512x520')
        self.game_window.resizable(False, False)
        self.game_window.title("Крестики-Нолики")
        self.buttons = [[tk.Button(self.game_window, text='', font=('normal', 30), width=7,height=3, cursor='hand2',
                                   command= lambda row=i, col=j: self.tap(row, col)) for j in range(3)] for i in range(3)]
        for i in range(3): #для кнопок по рядам
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)
                self.buttons[i][j].bind("<Enter>", self.enter_button)
                self.buttons[i][j].bind("<Leave>", self.leave_button)
        self.game_matrix = [['' for _ in range(3)] for _ in range(3)] #матрица для координат
        self.player_turn = True

    def enter_button(self, event): #подсветка при наведении на активную кнопку
        button = event.widget
        if button.cget('state') == tk.NORMAL:
            button.config(bg="light blue")
    def leave_button(self, event):
        button = event.widget
        if button.cget('state') == tk.NORMAL:
            button.config(bg="SystemButtonFace")

    def tap(self, row, col):#обработка нажатия
        if self.game_matrix[row][col] == '' and self.player_turn: #для хода игрока
            self.buttons[row][col].config(state=tk.DISABLED, text='X')
            self.game_matrix[row][col] = 'X'
            if self.check('X'):
                self.end_game('X')
            elif all([cell != '' for row in self.game_matrix for cell in row]):
                self.end_game('drawn_game')
            else:#для хода компьютера
                self.player_turn = False
                row, col = self.computer_move()
                self.game_matrix[row][col] = 'O'
                self.buttons[row][col].config(text='O', state=tk.DISABLED)
                if self.check('O'):
                    self.end_game('O')
                elif all([cell != '' for row in self.game_matrix for cell in row]):
                    self.end_game('drawn_game')
                else:
                    self.player_turn = True
    def computer_move(self): #расчет лучшего ходя для компьютера на основе минимакса
        best_score = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        for i in range(3):
            for j in range(3):
                if self.game_matrix[i][j] == '':
                    self.game_matrix[i][j] = 'O'
                    score = self.minimax(0, False, alpha, beta)
                    self.game_matrix[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                    alpha = max(alpha, score)
        return best_move
    def minimax(self, depth, is_maximizing, alpha, beta):#рекурсия для вычисления оценки с циклическим перебором ходов, используется альфа-бета отсечение для отбрасывания плохих ходов
        if self.check('X'):
            return -1 * depth
        elif self.check('O'):
            return depth
        elif all([cell != '' for row in self.game_matrix for cell in row]):
            return 0
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.game_matrix[i][j] == '':
                        self.game_matrix[i][j] = 'O'
                        score = self.minimax(depth + 1, False, alpha, beta)
                        self.game_matrix[i][j] = ''
                        best_score = max(best_score, score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.game_matrix[i][j] == '':
                        self.game_matrix[i][j] = 'X'
                        score = self.minimax(depth + 1, True, alpha, beta)
                        self.game_matrix[i][j] = ''
                        best_score = min(best_score, score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score
    def check(self, player):#проверка победы
        return any(all(cell == player for cell in row) for row in self.game_matrix) or \
               any(all(self.game_matrix[j][i] == player for j in range(3)) for i in range(3)) or \
               all(self.game_matrix[i][i] == player for i in range(3)) or \
               all(self.game_matrix[i][2 - i] == player for i in range(3))
    def eval(self):#анализ состояния игры
        if self.check('O'):
            return 1
        elif self.check('X'):
            return -1
        else:
            return 0
    def reset_game(self):# сброс для нвоой игры
        self.game_matrix = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].bind("<Enter>", self.enter_button)
                self.buttons[i][j].bind("<Leave>", self.leave_button)
                self.buttons[i][j].config(text='', state='normal', command=lambda row=i, col=j: self.tap(row, col))
        self.player_turn = True
    def end_game(self, result):#вывод о победе и закрытие\сброс
        messages = {'O': 'Бот выиграл.', 'X':'Вы выиграли!', 'drawn_game':'Ничья.'}
        message = messages.get(result, '')
        if message:
            answer = mb.askquestion('Игра окончена', f'{message} \n Сыграть ещё раз?')
            if answer == 'yes':
                self.reset_game()
            else:
                self.game_window.destroy()

def main(): #запуск самого окна
    login_window = LoginWindow()
    login_window.start()
if __name__ == "__main__":# Главная часть программы
    main()
