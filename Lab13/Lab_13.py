'''1.Прочитать в виде списков набор данных titanic.csv, взятый из открытых источников
   2.Для прочитанного набора выполнить обработку в соответствии со своим вариантом. Библиотекой pandas пользоваться нельзя.
Вариант 2. Определить количество мужчин и женщин  в 1,2 и 3 классе на борту и сколько из них выжило. '''
import csv #Инициализация словарей для хранения данных
counter_data = {'1': {'male': {'count': 0, 'survived': 0}, 'female': {'count': 0, 'survived': 0}},
              '2': {'male': {'count': 0, 'survived': 0}, 'female': {'count': 0, 'survived': 0}},
              '3': {'male': {'count': 0, 'survived': 0}, 'female': {'count': 0, 'survived': 0}}}
with open('titanic.csv', 'r') as file:
    reader = csv.DictReader(file)#Создаём объект для чтения файла как словаря
    for row in reader:
        pclass = row['Pclass']
        survived = int(row['Survived'])
        sex = row['Sex']
        counter_data[pclass][sex]['count'] += 1#Обновляем счетчики в словаре counter_data
        if survived == 1:
            counter_data[pclass][sex]['survived'] += 1
for pclass, gender_data in counter_data.items():
    for sex, data in gender_data.items():
        gender = 'Женщин' if sex == 'female' else 'Мужчин'
        print(f"{pclass}-й класс: {gender} - {data['count']}, Выжило - {data['survived']}")
