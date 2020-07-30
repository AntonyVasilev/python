# Task 3
"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

below_20 = []
salary_sum = 0.0
num_workers = 0

with open('salary.txt', encoding='utf-8') as f:
    for line in f:
        surname, salary = line.split()
        if float(salary) < 20000:
            below_20.append(surname)
        num_workers += 1
        salary_sum += float(salary)

print(f'Работники с окладом менее 20000.00 руб.: {below_20}')
print(f'Средний оклад: {salary_sum / num_workers:.2f} руб.')