# Task 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def num_division(num_1, num_2):
    """
    num_division(число_1, число_2)
    Выводит в терминал результат деления параметра num_1 на num_2. Предусмотрена обработка деления на ноль.
    :param num_1: 20
    :param num_2: 8
    :return: 20 / 8 -> 2.5
    """
    try:
        print(num_1 / num_2)
    except ZeroDivisionError:
        print('Вы ввели ноль.')


num_1, num_2 = input('Введите 2 числа через пробел: ').split()

try:
    num_division(float(num_1), float(num_2))
except ValueError:
    print('Вы ввели не число.')
