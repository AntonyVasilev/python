# Task 3
"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname} - {self.position}')

    def get_total_income(self):
        print(f'{self.name} {self.surname} заработал - {self.income["wage"] + self.income["bonus"]:.2f} руб.')


names = ['Александр', 'Виктор', 'Алексей']
surnames = ['Иванов', 'Петров', 'Сидоров']
positions = ['инженер', 'программист', 'аналитик']
incomes = [{"wage": 120000, "bonus": 50000}, {"wage": 150000, "bonus": 45000}, {"wage": 130000, "bonus": 55000}]

for i in range(3):
    worker = Position(names[i], surnames[i], positions[i], incomes[i])
    worker.get_full_name()
    worker.get_total_income()
