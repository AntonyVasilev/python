# Task 4
"""
Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go,
stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для
классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и
также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.colour = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернул {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/час')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Вы привысили разрешенную скорость!')
        else:
            print(f'Текущая скорость: {self.speed} км/час')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Вы привысили разрешенную скорость!')
        else:
            print(f'Текущая скорость: {self.speed} км/час')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if not self.is_police:
            print('Вы находитесь в полицейской машине незаконно!')
            exit()


# police_car = PoliceCar(85, 'white', 'Ford', False)
# police_car.go()

police_car = PoliceCar(85, 'white', 'Ford', True)
police_car.go()
police_car.show_speed()
police_car.stop()

work_car = WorkCar(44, 'green', 'Ford', False)
work_car.go()
work_car.turn('направо')
work_car.show_speed()
work_car.stop()

town_car = TownCar(58, 'black', 'Volvo', False)
town_car.go()
town_car.turn('налево')
town_car.show_speed()
town_car.turn('направо')
town_car.speed = 68
town_car.show_speed()
town_car.stop()

sport_car = SportCar(92, 'red', 'Porsche', False)
sport_car.go()
sport_car.turn('направо')
sport_car.turn('налево')
sport_car.show_speed()
sport_car.stop()
