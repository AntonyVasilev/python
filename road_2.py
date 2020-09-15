# Task 2
"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать
защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:


    def __init__(self, length, width):
        self.length = length
        self.width = width

    def weight_count(self):
        asphalt_weight = self.length * self.width * 25 * 5
        return asphalt_weight / 1000


road = Road(15, 10000)

print(f'{road.weight_count()} т.')