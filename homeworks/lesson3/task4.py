"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_range_int(num_from=1, num_to=3, step=1):
    """
    Возвращает генератор для последовательности целых чисел от starting_from до up_to включительно с шагом step
    шаг всегда прибаляется
    :param num_from: начало последовательности (1 по умолчанию)
    :param num_to: конец последовательности (3 по умолчанию)
    :param step: шаг (1 по умолчанию) может быть положительным или отрицательным целым числом
    :return: генератор последовательности
    """
    if type(num_from) is not int or type(num_to) is not int or type(step) is not int:
        raise TypeError('my_range_n принимает только целые числа и целый шаг')

    if num_from < num_to:
        if step < 0:
            raise ValueError('Введенные параметры приведут к бесконечной последовательности')
        num_from -= step
        while num_from < num_to - step:
            num_from += step
            yield num_from

    if num_from > num_to:
        if step > 0:
            raise ValueError('Введенные параметры приведут к бесконечной последовательности')
        num_from -= step
        while num_from > num_to + step and step < 0:
            num_from += step
            yield num_from


def my_func(x, y):
    """
    Возводит число x в степень с отрицательным показателем y
    :param x: действительное число
    :param y: целое отрицательное число (целое положительное число будет преобразовано в отрицательное)
    :return: число x в степени y
    """
    if type(x) is not float and type(x) is not int:
        raise TypeError('основание степени должно быть действительным или целым числом')
    if y == 0 or x == 0:
        raise ValueError('И основание и показатель степени для нашей задачи не могут быть равны 0')

    if y > 0:
        y = -1 * y
    result1 = x ** y
    result2 = x

    for _ in my_range_int(1, int(-y)):
        result2 = result2 * x

    return result1, 1 / result2


# main
try:
    x_in = float(input('Введите x\n>>>'))
    y_in = float(input('Введите y\n>>>'))

    variant1, variant2 = my_func(x_in, y_in)
    print(f'Результат x**y: {variant1}\nРезультат my_func(x, y): {variant2}')
except TypeError as t:
    print(str(t))
except ValueError as v:
    print(str(v))
