# Task 5
"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""

with open('numbers.txt', 'w') as f:
    f.writelines('18 42 31 6 26')

with open('numbers.txt') as f:
    numbers_line = f.readline()

numbers = numbers_line.split()
result = 0

for number in numbers:
    result += int(number)

print(f'Сумма чисел в файле равна {result}')
