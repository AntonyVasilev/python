# Task 1
"""
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, user_date):
        self.user_date = user_date

    @classmethod
    def to_num(cls, usr_date):
        usr_year, usr_month, usr_day= usr_date.split('-')
        return int(usr_year), int(usr_month), int(usr_day)

    @staticmethod
    def validation(usr_year, usr_month, usr_date):
        is_month = True if 0 < usr_month < 13 else False
        is_year = True if usr_year < 2100 else False
        if usr_month in [1, 3, 5, 7, 8, 10, 12] and 0 < usr_date <= 31:
            is_day = True
        elif usr_month in [4, 6, 9, 11] and 0 < usr_date <= 30:
            is_day = True
        elif usr_month == 2 and usr_year % 4 == 0 and 0 < usr_date <= 29:
            is_day = True
        elif usr_month == 2 and usr_year % 4 != 0 and 0 < usr_date <= 28:
            is_day = True
        else:
            is_day = False
        print(f'Validation result: year - {is_year}, month - {is_month}, day - {is_day}')


year, month, day = Date.to_num('2019-02-29')
print(year, month, day)
Date.validation(year, month, day)
