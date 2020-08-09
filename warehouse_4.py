# Task 4
"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы
— конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self, num_storage_cells, storey, cells_in_row):
        """
        Задаются общие параметры склада. Расчитывается количество рядов стеллажей
        :param num_storage_cells: Общее количество ячее для хранения
        :param storey: Количество ярусов хранения на стеллаже
        :param cells_in_row: Количество ячеек для хранения в ряду
        """
        self.num_storage_cells = num_storage_cells
        self.storey = storey
        self.cells_in_row = cells_in_row


class OfficeEquipment:
    def __init__(self, name, model, quantity, price):
        """
        Клас Оргтехника
        :param name: Наименование производителя
        :param model: Модель
        :param quantity: Количество
        :param price: Цена
        """
        self.name = name
        self.model = model
        self.quantity = quantity
        self.price = price


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Copier(OfficeEquipment):
    pass
