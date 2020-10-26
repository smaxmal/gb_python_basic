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
        if result is None:
            result = item
        result = func(result, item)
    return result
