# Task 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

count_l = 0
count_w = 0

with open('count_text.txt') as f:
    for line in f:
        count_l += 1
        count_w += len(line.split())
        print(f'В строке {count_l} находится {len(line.split())} слов(а)')

print(f'Всего строк: {count_l}')
print(f'Всего слов: {count_w}')
