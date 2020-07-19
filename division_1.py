# Task 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def num_division(num_1, num_2):
    try:
        print(num_1 / num_2)
    except ZeroDivisionError:
        print('Вы ввели ноль.')


num_1, num_2 = input('Введите 2 числа через пробел: ').split()
num_division(float(num_1), float(num_2))
