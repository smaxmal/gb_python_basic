"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        try:
            self._income = {'wage': int(wage), 'bonus': int(bonus)}
        except TypeError:
            raise TypeError('Зарплата должна быть указана числом')


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        """ Возвращает полное имя сотрудника """
        return f'{self.name} {self.surname}'

    def get_full_income(self):
        """ Возвращает полный доход сотрудника"""
        return self._income['wage'] + self._income['bonus']


# main
test_data = (('Иван', 'Петров', 'рабочий', 30000, 5000), 'рабочий', 'Иван Петров', 35000)
worker_a = Position(*test_data[0])

assert worker_a.position == test_data[1], 'Позиция сохранена некорректно'
assert worker_a.get_full_name() == test_data[2], 'Полное имя составляется некорректно'
assert worker_a.get_full_income() == test_data[3], 'Полный доход подсчитан неправильно'

print(f'Сотрудник {worker_a.get_full_name()} на должности {worker_a.position} получает полный доход '
      f'{worker_a.get_full_income()}р')
