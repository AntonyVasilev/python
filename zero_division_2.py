# Task 2
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на нуль. Проверьте его работу на данных, вводимых пользователем. При
вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


number = float(input('Input number: '))
try:
    divisor = float(input('Input divisor: '))
    if divisor == 0:
        raise MyZeroDivision('Zero division forbidden!')
except MyZeroDivision as err:
    print(err)
else:
    print(number / divisor)
