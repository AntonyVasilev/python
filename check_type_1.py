# Task 1
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['my new list', 519, True, 15.998, ('test', 11)]

for item in my_list:
    print(type(item))
