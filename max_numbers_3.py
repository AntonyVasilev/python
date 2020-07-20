# Task 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """
    my_func(число_1, число_2, число_3)
    Возвращает сумму наибольших двух аргументов.
    :param a: 15
    :param b: 5
    :param c: 10
    :return: 15 + 10 -> 25
    """
    user_list = [a, b, c]
    user_list.remove(min(user_list))
    return user_list[0] + user_list[1]

items = []
for i in range(3):
    items.append(int(input(f'Введите число {i+1}: ')))

print(my_func(items[0], items[1], items[2]))
