"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod
from random import randrange


class Cloth(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @size.setter
    def size(self, value):
        pass

    @property
    @abstractmethod
    def fabric_needed(self):
        pass


class Coat(Cloth):

    def __init__(self, name='пальто'):
        self.__name = name
        self.__size = 0

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def fabric_needed(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Cloth):

    def __init__(self, name='костюм'):
        self.__name = name
        self.__size = 0

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def fabric_needed(self):
        return round(self.__size * 2 + 0.3, 2)


class ProductionLine:

    def __init__(self):
        self.__fabric_suit = 0
        self.__fabric_coat = 0
        self.__cloth_list = []

    def fill_the_line(self):
        """ Заполняет линию одежды из 5 товаров случайным числом пальто и костюмов со случайным размером
        """
        for _ in range(5):
            if randrange(0, 100) % 2:
                suit = Suit()
                suit.size = randrange(32, 58, 2)
                self.__fabric_suit += suit.fabric_needed
                self.__cloth_list.append(suit)
            else:
                coat = Coat()
                coat.size = randrange(32, 58, 2)
                self.__fabric_coat += coat.fabric_needed
                self.__cloth_list.append(coat)

    def __str__(self):
        result = ''
        for cloth in self.__cloth_list:
            result += f'Заказали {cloth.name} {cloth.size} размера, на него уйдет {cloth.fabric_needed}м ткани\n'

        return result + f'\nНам понадобится {self.__fabric_coat}м ткани на пальто и {self.__fabric_suit}м ' \
                        f'ткани на костюмы\n\n' \
                        f'Всего ткани понадобится: {self.__fabric_coat + self.__fabric_suit}м'


# main
production_line = ProductionLine()
production_line.fill_the_line()
print(production_line)
