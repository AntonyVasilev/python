# Task 3
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени
# года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = 0

while month > 12 or month <= 0:
    try:
        month = int(input('Введите номер месяца: '))
    except ValueError:
        print('Вы ввели не номер месяца.')


# Решение через список

if month == 12:
    month = 0  # Присвоение Декабрь индекса 0 для более удобной работы со списком

months_list = ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май',
               'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь']

if 0 <= month <= 2:
    print(f'{months_list[month]} - зимний месяц.')
elif 3 <= month <= 5:
    print(f'{months_list[month]} - весенний месяц.')
elif 6 <= month <= 8:
    print(f'{months_list[month]} - летний месяц.')
else:
    print(f'{months_list[month]} - осенний месяц.')


# Второе решение через словарь

months_dict = {0: 'Декабрь', 1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май',
               6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь'}

if 0 <= month <= 2:
    print(f'{months_dict[month]} - зимний месяц.')
elif 3 <= month <= 5:
    print(f'{months_dict[month]} - весенний месяц.')
elif 6 <= month <= 8:
    print(f'{months_dict[month]} - летний месяц.')
else:
    print(f'{months_dict[month]} - осенний месяц.')


# Решение через словарь и список

months_list3 = ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май',
                'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь']
months_dic3 = {0: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
               6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень'}

print(f'{months_list3[month]} - {months_dic3[month]}')
print(f'Сейчас {months_dic3[month]}')