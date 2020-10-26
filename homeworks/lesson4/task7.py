"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!. Подсказка:
факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

import homeworks.lesson4.my_functions as myf


def fact(n):
    """ fact(n) -> generator object    """

    if type(n) is str:
        try:
            n = int(n)
        except TypeError:
            raise TypeError('fact принимает только числа или строки, которые можно привести к числу')

    if type(n) is not int and type(n) is not float:
        raise TypeError('fact принимает только числа или строки, которые можно привести к числу')

    result = 1
    for idx in myf.my_range_int(1, n + 1):
        result *= idx
        yield result


end_num = input('Для функции n! введите n\n>>>')
if end_num.isnumeric():
    print([el for el in fact(end_num)])
else:
    print('Надо было вводить число')
