"""
 Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func(first, second, third):
    try:
        if first > third and second > third:
            return first + second
        elif second > first and third > first:
            return second + third
        else:
            return first + third
    except TypeError:
        return None


# main

try:
    first_in = float(input('Введите первое число \n>>>'))
    second_in = float(input('Введите первое число \n>>>'))
    third_in = float(input('Введите первое число \n>>>'))
    print(f'Сумма двух самых больших чисел: {my_func(first_in, second_in, third_in)}')
except ValueError:
    print('Надо было число вводить')
