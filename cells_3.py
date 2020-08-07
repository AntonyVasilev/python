# Task 3
"""
Реализовать программу работы с органическими клетками. Необходимо создать
класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание
(__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы
должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, num_sells):
        self.num_sells = num_sells

    def make_order(self, cells_in_row):
        self.cells_in_row = cells_in_row
        if type(self.num_sells) != int:
            return
        else:
            cell = ''
            j = 0
            for i in range(self.num_sells):
                j += 1
                cell += '*'
                if j == self.cells_in_row:
                    cell += '\n'
                    j = 0
            return cell

    def __add__(self, other):
        self.other_cell = other.num_sells
        return self.num_sells + self.other_cell

    def __sub__(self, other):
        self.other_cell = other.num_sells
        result = self.num_sells - self.other_cell
        if result > 0:
            return result
        else:
            return 'Вычитаемая клетка больше исходной'

    def __mul__(self, other):
        self.other_cell = other.num_sells
        return self.num_sells * self.other_cell

    def __truediv__(self, other):
        self.other_cell = other.num_sells
        return self.num_sells // self.other_cell


cell_1 = Cell(14)
cell_2 = Cell(4)

sum_cells = cell_1 + cell_2
print(sum_cells)
cell_3 = Cell(sum_cells)
print(cell_3.make_order(10))

sub_cells = cell_1 - cell_2
print(sub_cells)
cell_4 = Cell(sub_cells)
print(cell_4.make_order(4))

mul_cells = cell_1 * cell_2
print(mul_cells)
cell_5 = Cell(mul_cells)
print(cell_5.make_order(15))

div_cells = cell_1 / cell_2
print(div_cells)
cell_6 = Cell(div_cells)
print(cell_6.make_order(5))
