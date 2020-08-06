# Task 1
"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список
списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
"""

from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result_line = ''
        for line in self.matrix:
            for item in line:
                result_line += str(item) + ' '
            result_line += '\n'
        return result_line

    def __add__(self, other):
        self.other_matrix = other.matrix
        result_matrix = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[i][j] = self.matrix[i][j] + self.other_matrix[i][j]
        return result_matrix


matrix_list_1 = [[5, 8, 4], [9, 1, 3], [7, 1, 8]]
matrix_list_2 = [[9, 1, 4], [2, 2, 5], [8, 3, 7]]
matrix_1 = Matrix(matrix_list_1)
matrix_2 = Matrix(matrix_list_2)

result = matrix_1 + matrix_2
matrix_res = Matrix(result)
print(matrix_res)
