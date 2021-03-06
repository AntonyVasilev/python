# Task 3
"""
Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу
исключения на реальном примере. Необходимо запрашивать у
пользователя данные и заполнять список. Класс-исключение должен
контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются
бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается,
сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может
вводить только числа и строки. При вводе пользователем очередного
элемента необходимо реализовать проверку типа элемента и вносить
его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить
соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class IsNotDigit(Exception):
    def __init__(self, text):
        self.text = text


num_list = []

while True:
    try:
        user_input = input('Input number (stop to quit): ')
        if user_input == 'stop':
            break
        elif user_input.isdigit():
            num_list.append(int(user_input))
        else:
            raise IsNotDigit('Only digits accepted!')
    except IsNotDigit as err:
        print(err)

print(num_list)
