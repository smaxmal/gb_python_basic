def my_range_int(num_from=1, num_to=3, step=1):
    """ my_range (num_from num_to step) -> generator object

    Возвращает генератор для последовательности целых чисел от num_from до num_to включительно с шагом step
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


def my_reduce(func, iterable):
    """ my_reduce(func, iterable]) -> cumulative result

    my_reduce последоватнльно применяет функцию func к элементам последовательности iterable

    :param func:функция, принимающая два позиционных аргумента. Первый аргумент - накопительный итог выполнения,
                второй - текущий элемент послеовательности
    :param iterable:
    :return:
    """
    result = None
    for item in iterable:
        result = func(result, item)
    return result


def my_round(x, y=0):
    """ rounds x to y (0 by default) number of decimals
    """

    multiplier = 10 ** y
    x = x * multiplier
    x = (x + 0.5) // 1
    x = x / multiplier
    return x


def my_sum(iterable):
    """ Summarize numeric values in iterable
    """
    result = 0
    for item in iterable:
        try:
            number = float(item)
            if number.is_integer():
                number = int(item)
        except TypeError:
            raise ValueError('my_sum принимает только последовательность элементов, приводимых к числам int или float')

        result += number

    return result


def my_map(func, iterable):
    """ Выполняет заданное func преобразование для каждого эелемента iterable
    """

    for item in iterable:
        yield func(item)
