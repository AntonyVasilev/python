"""
Task 4
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы
— конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Task 5
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о
наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.

Task 6
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""

from math import ceil


class NotNumErr(Exception):
    def __init__(self, text):
        self.text = text


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
        self.rows = ceil(self.num_storage_cells / (self.storey * cells_in_row))
        self.items_list = []
        self.unit_items = []

    def add_to_wh(self, item_id, make, name, model, quantity, type):
        try:
            self.item_id = item_id
            self.quantity = quantity
            if not str(self.item_id).isdigit() or not str(self.quantity).isdigit():
                raise NotNumErr('ID или количество не число!')
        except NotNumErr as err:
            print(err)
        else:
            self.make = make
            self.name = name
            self.model = model
            self.type = type
            add_dict = {'item_id': self.item_id, 'make': self.make, 'name': self.name, 'model': self.model,\
                    'quantity': self.quantity, 'type': self.type}
            self.items_list.append(add_dict)

    def ship_from_wh(self, item_id, make, name, model, quantity, type):
        try:
            self.item_id = item_id
            self.quantity = quantity
            if not str(self.item_id).isdigit() or not str(self.quantity).isdigit():
                raise NotNumErr('ID или количество не число!')
        except NotNumErr as err:
            print(err)
        else:
            self.make = make
            self.name = name
            self.model = model
            self.type = type
            pop_dict = {'item_id': self.item_id, 'make': self.make, 'name': self.name, 'model': self.model,\
                    'quantity': self.quantity, 'type': self.type}
            self.items_list.remove(pop_dict)

    def transfer_to_unit(self, item_id, make, name, model, quantity, type):
        try:
            self.item_id = item_id
            self.quantity = quantity
            if not str(self.item_id).isdigit() or not str(self.quantity).isdigit():
                raise NotNumErr('ID или количество не число!')
        except NotNumErr as err:
            print(err)
        else:
            self.make = make
            self.name = name
            self.model = model
            self.type = type
            pop_dict = {'item_id': self.item_id, 'make': self.make, 'name': self.name, 'model': self.model,\
                    'quantity': self.quantity, 'type': self.type}
            self.items_list.remove(pop_dict)
            self.unit_items.append(pop_dict)

    def print_remainders(self, print_type):
        self.print_type = print_type
        if self.print_type == 'wh':
            print(self.items_list)
        elif self.print_type == 'unit':
            print(self.unit_items)
        else:
            print('Не верный параметр печати')


class OfficeEquipment:
    def __init__(self, item_id, make, name, model, quantity, price, connect_types, weight, dimensions, duplex, colour):
        """
        Клас Оргтехника
        :param item_id: Код оборудования
        :param make: Марака устройства
        :param name: Наименование устройства
        :param model: Модель
        :param quantity: Количество
        :param price: Цена
        :param connect_types: Типы подключения устройства (кабель USB, Wi-Fi, Ethernet)
        :param weight: Вес устройства
        :param dimensions: Размеры устройства
        :param duplex: Наличие модуля двухсторонней печати/сканирования (True/False)
        :param colour: Цвет устройства
        """
        self.item_id = item_id
        self.make = make
        self.name = name
        self.model = model
        self.quantity = quantity
        self.price = price
        self.connect_types = connect_types
        self.weight = weight
        self.dimensions = dimensions
        self.duplex = duplex
        self.colour = colour


class Printer(OfficeEquipment):
    def __init__(self, colour_print, print_speed, max_print_resolution):
        """
        Класс Принтер
        :param colour_print: Возможность цветной печати (True/False)
        :param print_speed: Скорость печати
        :param max_print_resolution: Максимальное разрешение печати
        """
        self.colour_print = colour_print
        self.print_speed = print_speed
        self.max_print_resolution = max_print_resolution


class Scanner(OfficeEquipment):
    def __init__(self, scan_speed, max_scan_resolution, scan_type):
        """
        Класс Сканер
        :param scan_speed: Скорость сканирования
        :param max_scan_resolution: Максимальное разрешение сканирования
        :param scan_type: Тип сканера (планшетный/с полистовой подачей)
        """
        self.scan_speed = scan_speed
        self.max_scan_resolution = max_scan_resolution
        self.scan_type = scan_type


class Copier(OfficeEquipment):
    def __init__(self, copy_speed, max_copy_resolution):
        """
        Класс Копир
        :param copy_speed: Скорость копирования
        :param max_copy_resolution: Максимальное разрешение копирования
        """
        self.copy_speed = copy_speed
        self.max_copy_resolution = max_copy_resolution


wh_1 = Warehouse(1000, 2, 20)
wh_1.add_to_wh(1, 'HP', 'LaserJet Enterprise M612dn', '7PS86A', 10, 'printer')
wh_1.add_to_wh(2, 'Xerox', 'Phaser 3052', '3052V/NI', 8, 'printer')
wh_1.add_to_wh(3, 'Xerox', 'Duplex Portable Scanner', '100N03261', 20, 'scanner')
wh_1.print_remainders('wh')

wh_1.transfer_to_unit(2, 'Xerox', 'Phaser 3052', '3052V/NI', 8, 'printer')
wh_1.print_remainders('wh')
wh_1.print_remainders('unit')

wh_1.ship_from_wh(1, 'HP', 'LaserJet Enterprise M612dn', '7PS86A', 10, 'printer')
wh_1.print_remainders('wh')
