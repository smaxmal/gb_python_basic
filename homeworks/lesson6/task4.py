"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """ go() -> str """

        return f'{self.color} {self.name} поехала'

    def turn(self, direction):
        """ turn(direction: str) -> str """

        possible_directions = ('налево', 'направо')
        if direction not in possible_directions:
            raise ValueError('Разрешены повороты только "налево" или "направо"')

        return f'{self.color} {self.name} поворачивает {direction}'

    def stop(self):
        """ stop() -> str """

        return f'{self.color} {self.name} останавливается\n'

    def show_speed(self):
        """ show_speed() -> str """

        return f'{self.color} {self.name} едет со скоростью {self.speed}.'


class TownCar(Car):

    def __init__(self, color, name):
        self.speed_limit = 60
        super().__init__(color, name)

    def show_speed(self):
        """ show_speed() -> str """

        msg = super().show_speed()
        if self.speed > self.speed_limit:
            msg = msg + f' Внимание, превывышение макисмальной разрешенной скорости на {self.speed - self.speed_limit}!'
        return msg


class SportCar(Car):

    def __init__(self, color, name):
        self.speed_limit = 60
        super().__init__(color, name)


class WorkCar(Car):

    def __init__(self, color, name):
        self.speed_limit = 40
        super().__init__(color, name)

    def show_speed(self):
        """ show_speed() -> str """

        msg = super().show_speed()
        if self.speed > self.speed_limit:
            msg = msg + f' Внимание, превывышение макисмальной разрешенной скорости на {self.speed - self.speed_limit}!'
        return msg


class PoliceCar(Car):

    def __init__(self, color, name):
        self.speed_limit = 60
        super().__init__(color, name, True)


# main
kia = TownCar('Синяя', 'Kia Sportage')
print(kia.go())
kia.speed = 55
print(kia.show_speed())
print(kia.turn('налево'))
kia.speed = 80
print(kia.show_speed())
print(kia.stop())

ferrari = SportCar('Красная', 'Ferrari 488')
print(ferrari.go())
ferrari.speed = 80
print(ferrari.show_speed())
print(ferrari.turn('направо'))
ferrari.speed = 150
print(ferrari.show_speed())
if not ferrari.is_police:
    print('А ведь не полиция ...\n')

cat = WorkCar('Жёлтый', 'Caterpillar 415 IL')
print(cat.go())
cat.speed = 30
print(cat.show_speed())
print(cat.turn('направо'))
cat.speed = 50
print(cat.show_speed())
print(cat.stop())

police = PoliceCar('Синяя', 'BMW X5')
print(police.go())
police.speed = 80
print(police.show_speed())
print(police.turn('налево'))
police.speed = 120
print(police.show_speed())
if police.is_police:
    print('Полиции можно')
print(police.stop())
