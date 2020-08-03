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
    length = float
    width = float
    weight = 25
    thickness = float

    def weight_count(self, length, width, thinkness):
        self.length = length
        self.width = width
        self.thickness = thinkness
        asphalt_weight = length * width * self.weight * thinkness
        return asphalt_weight


road = Road()

print(f'{road.weight_count(15, 10000, 5) / 1000} т.')
