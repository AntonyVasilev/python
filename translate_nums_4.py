# Task 4
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""
numbers = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять'}

with open('eng_numbers.txt') as eng_f:
    for line in eng_f:
        eng_num, num = line.split(' - ')
        with open('rus_numbers.txt', 'a', encoding='utf-8') as rus_f:
            rus_line = numbers[num.strip()] + ' - ' + num
            rus_f.writelines(rus_line)
