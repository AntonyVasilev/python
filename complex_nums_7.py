# Task 7
"""
Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNums:
    def __init__(self, c_num):
        self.c_num = c_num

    def __add__(self, other):
        self.c_other_num = other.c_num
        # print(self.c_num, self.c_other_num)
        return self.c_num + self.c_other_num

    def __mul__(self, other):
        self.c_other_num = other.c_num
        return self.c_num * self.c_other_num


user_nums = []
for i in range(2):
    x = float(input(f'Введите действительную часть комплексного числа {i + 1}: '))
    y = float(input(f'Введите мнимую часть комплексного числа {i + 1}: '))
    user_nums.append(complex(x, y))

c_num_1 = ComplexNums(user_nums[0])
c_num_2 = ComplexNums(user_nums[1])

c_num_1 + c_num_2
print(c_num_1 + c_num_2)
print(c_num_1 * c_num_2)
