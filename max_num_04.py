# Задание 4

user_number = int(input('Введите целое положительное число: '))

while user_number < 0:
    print('Вы ввели отрицательное число.')
    user_number = int(input('Введиете число от 0 до 9: '))

digit = user_number
digits = []
i = 0

# Создаю список с цифрами из введенного числа
while digit > 0:
    digits.append(digit % 10)
    digit = digit // 10
    i += 1
print(digits)

# Сравниваю числа из списка и нахожу наибольшше
max_num = digits[0]
# print(max_num)
i = 1
# print(len(digits))
count = len(digits)

while i < count:
    if digits[i] > max_num:
        max_num = digits[i]
    # print(max_num)
    i += 1

print(f'Максимальная цифра в введенном числе: {max_num}')
