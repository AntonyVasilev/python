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
    name = str
    surname = str
    position = str
    _income = {'wage': 0, 'bonus': 0}


class Position(Worker):

    def get_full_name(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        print(f'{name} {surname} - {position}')

    def get_total_income(self, name, surname, income):
        self.name = name
        self.surname = surname
        self._income = income
        print(f'{name} {surname} заработал - {income["wage"] + income["bonus"]:.2f} руб.')


names = ['Александр', 'Виктор', 'Алексей']
surnames = ['Иванов', 'Петров', 'Сидоров']
positions = ['инженер', 'программист', 'аналитик']
incomes = [{"wage": 120000, "bonus": 50000}, {"wage": 150000, "bonus": 45000}, {"wage": 130000, "bonus": 55000}]

worker = Position()
for i in range(3):
    worker.get_full_name(names[i], surnames[i], positions[i])
    worker.get_total_income(names[i], surnames[i], incomes[i])