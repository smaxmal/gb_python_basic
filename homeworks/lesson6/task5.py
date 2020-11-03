"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:

    def __init__(self, name='Канц товар'):
        self.name = name

    def draw(self):
        """ draw() -> str """

        msg = 'Запуск отрисовки'
        print(msg)
        return msg


class Pen(Stationary):

    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        """ draw() -> str """

        msg = 'Это ручка и она пишет'
        print(msg)
        return msg


class Pencil(Stationary):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        """ draw() -> str """

        msg = 'Это карандаш и он рисует'
        print(msg)
        return msg


class Handle(Stationary):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        """ draw() -> str """

        msg = 'Это маркер, а вовсе не Handle, и он отмечает'
        print(msg)
        return msg


# main
test_data = {'Канц товар': 'Запуск отрисовки', 'Ручка': 'Это ручка и она пишет', 'Карандаш': 'Это карандаш и он рисует',
             'Маркер': 'Это маркер, а вовсе не Handle, и он отмечает'}
stationary = Stationary()
pen = Pen()
pencil = Pencil()
handle = Handle()

try:
    assert stationary.draw() == test_data[stationary.name]
    assert pen.draw() == test_data[pen.name]
    assert pencil.draw() == test_data[pencil.name]
    assert handle.draw() == test_data[handle.name]
except KeyError:
    raise AssertionError('name какой-то получился неправильный')

print('\nВсе работает!')
