"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div_numbers(x=0.0, y=1.0):

    try:
        return x / y
    except ZeroDivisionError:
        return float('nan')


# main

try:
    number_x = float(input('Введите X:\n>>>'))
    number_y = float(input('Введите Y:\n>>>'))
    print(div_numbers(number_x, number_y))
except ValueError:
    print('Надо было воодить число')
