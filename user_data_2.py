# Task 2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_user_data(name, surname, year, city, email, phone):
    """
    print_user_data(имя, фамилия, год рождения, город проживания, email, номер телефона)
    Выводит данные о пользователе в терминал одной строкой.
    :param name: Иван
    :param surname: Иванов
    :param year: 1990
    :param city: Москва
    :param email: ivan@ivanov.ru
    :param phone: 9876543210
    :return: Имя - Иван, фамилия - Иванов, дата рождения - 1990 г., город проживания - Москва,
     адрес электронной почты - ivan@ivanov.ru, номер телефона - 9876543210
    """
    print(
        f'Имя - {name}, фамилия - {surname}, дата рождения - {year} г., город проживания - {city},'
        f' адрес электронной почты - {email}, номер телефона - {phone}')


user_data = {'имя': '', 'фамилия': '', 'год рождения': '', 'город проживания': '', 'email': '', 'телефон': ''}
for key in user_data.keys():
    value = [key, int(input(f'Введите - {key}: ')) if key == 'год рождения' or key == 'телефон'
    else input(f'Введите - {key}: ')]
    user_data.update([value])

print_user_data(name=user_data['имя'], surname=user_data['фамилия'], year=user_data['год рождения'],
                city=user_data['город проживания'], email=user_data['email'], phone=user_data['телефон'])
