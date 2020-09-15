# Задание 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в
# числе. Для решения используйте цикл while и арифметические операции.

user_number = int(input('Введите целое положительное число: '))

# Проверка корректности ввода
while user_number < 0:
    print('Вы ввели отрицательное число.')
    user_number = int(input('Введиете целое положительное число: '))

max_num = 0
digit = user_number

while user_number > 0:
    digit = user_number % 10
    user_number = user_number // 10
    if digit > max_num:
        max_num = digit
    # print(max_num)

print(f'Максимальная цифра в введенном числе: {max_num}')
