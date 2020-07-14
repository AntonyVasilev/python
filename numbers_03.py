# Задание 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = int(input('Введиете положительное число: '))

while user_number < 0:
    print('Вы ввели отрицательное число.')
    user_number = int(input('Введиете число от 0 до 9: '))

number_1 = user_number
number_2 = int(str(user_number) + str(user_number))
number_3 = int(str(user_number) + str(user_number) + str(user_number))
# print(number_1, number_2, number_3)

result = number_1 + number_2 + number_3
print(result)
