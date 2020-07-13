# Задание 6

a = float(input('Введите дистанцию первой пробежки в километрах: '))
b = float(input('Введите ежедневную дистанцию пробежки, которую вы хотите достичь: '))
days_count = 1

while a < b:
    a = a * 1.1
    days_count += 1
    # print(a, days_count)

print(f'Вы достигните цели на {days_count}-й день.')