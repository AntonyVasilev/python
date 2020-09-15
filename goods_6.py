# Task 6
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
# — номер товара и словарь с параметрами (характеристиками товара: название, цена,
# количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

import copy

goods = []  # Итоговый список данных
product = ()  # Отдельного товар
prod_spec = {}  # Словарь характеристик
new_item = []
i = 0  # Код товара

# Заполнение списка данными от пользователя

while True:
    name = input('Введите наименование товара: ')
    price = float(input('Введите цену за еденицу: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите еденицу измерения товара: ')
    prod_spec.update({'наименование': name})
    prod_spec.update({'цена': price})
    prod_spec.update({'количество': quantity})
    prod_spec.update({'ед': unit})
    product = (i, prod_spec)
    new_item.append(product)
    goods.extend(copy.deepcopy(new_item))
    new_item.clear()
    i += 1
    user_answer = input('Вы хотите ввести еще один товар (да - да, остальное - нет)?: ')
    if user_answer == 'да':
        continue
    else:
        break

# print(goods)

# Аналитика товара

result_dict = {}
name_list = []
price_list = []
quantity_list = []
unit_list = []

for index, products in goods:
    specification = products
    name = specification.get('наименование')
    price = specification.get('цена')
    quantity = specification.get('количество')
    unit = specification.get('ед')
    if name not in name_list:
        name_list.extend([name])
    if price not in price_list:
        price_list.extend([price])
    if quantity not in quantity_list:
        quantity_list.extend([quantity])
    if unit not in unit_list:
        unit_list.extend([unit])

result_dict.update({'наименование': name_list})
result_dict.update({'цена': price_list})
result_dict.update({'количество': quantity_list})
result_dict.update({'ед': unit_list})

print(result_dict)
