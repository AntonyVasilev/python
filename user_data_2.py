# Task 2
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_user_data(**kwargs):
    """
    print_user_data(имя, фамилия, год рождения, город проживания, email, номер телефона)
    Выводит данные о пользователе в терминал одной строкой.
    :param kwargs: Получает словарь именованных параметров
    :return: Имя - Иван, фамилия - Иванов, дата рождения - 1990 г., город проживания - Москва,
    адрес электронной почты - ivan@ivanov.ru, номер телефона - phone
    """
    print(f"Имя - {kwargs['name']}, фамилия - {kwargs['surname']}, дата рождения - {kwargs['year']} г., "
        f"город проживания - {kwargs['city']}, адрес электронной почты - {kwargs['email']}, "
        f"номер телефона - {kwargs['phone']}")


user_data = {'имя': '', 'фамилия': '', 'год рождения': '', 'город проживания': '',
             'email': '', 'телефон': ''}
for key in user_data.keys():
    value = [key, int(input(f'Введите - {key}: ')) if key == 'год рождения' or key == 'телефон'
    else input(f'Введите - {key}: ')]
    user_data.update([value])

print_user_data(name=user_data['имя'], surname=user_data['фамилия'], year=user_data['год рождения'],
                city=user_data['город проживания'], email=user_data['email'], phone=user_data['телефон'])
