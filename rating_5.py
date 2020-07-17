# Task 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных
# чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

my_list = [8, 6, 5, 3, 3, 2, 1, 1]
new_number = 0

while new_number <= 0:
    try:
        new_number = int(input('Введите рейтинг: '))
    except ValueError:
        print('Вы ввели не целое число.')

for i in range(len(my_list)):
    if new_number > my_list[i]:
        my_list.insert(i, new_number)
        break
    elif new_number <= my_list[len(my_list) - 1]:
        my_list.append(new_number)
        break

print(my_list)
