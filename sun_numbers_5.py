# Task 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале
# нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def input_numbers():
    """
    Функция получает от пользователя строку цифр, введенных через пробел и разбивает их на отдельные
    элементы для формирования списка с цифрами. Если пользователь вводит симфол 'q', маркеру
    stop_sign присваивается значение True для учета желания пользователя завершить программу.
    Возврашает кортеж с списком чисел и значением маркера завершения программы.
    :return: ([a, b, c, ...], True/False)
    """
    new_list = []
    stop_sign = False
    input_list = input('Введите список чисел через пробел (q - выход): ')
    num_list = input_list.split()
    for i, item in enumerate(num_list):
        if num_list[i].isdigit():
            new_list.append(int(item))
        elif num_list[i].lower() == 'q':
            stop_sign = True
    return new_list, stop_sign

def sum_numbers(numbers):
    """
    sum_numbers(список чисел)
    Функция принимает список чисел, введенных пользователем, и возвращает их сумму.
    :param numbers: [15, 25, 10]
    :return: 50
    """
    result = 0
    for number in numbers:
        result += number
    return result

result = int()
exit_sign = False

while exit_sign != True:
    numbers, exit_sign = input_numbers()
    result += sum_numbers(numbers)
    print(f'Сумма введенных чисел равна {result}')