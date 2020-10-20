"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
var_list = [3, 'hello', 5.4, True, [5, 6, 7], (5, "five"), {1: 'code'}, {8, 9, 0}]

for item in var_list:
    if type(item) is int:
        print(item, ' - Это Int')
    elif type(item) is float:
        print(item, ' - Это float')
    elif type(item) is str:
        print(item, ' - Это string')
    elif type(item) is bool:
        print(item, ' - Это bool')
    elif type(item) is list:
        print(item, ' - Это list')
    elif type(item) is tuple:
        print(item, ' - Это tuple')
    elif type(item) is dict:
        print(item, ' - Это dictionary')
    elif type(item) is set:
        print(item, ' - Это set')
    else:
        print('Это я не учел, а тип у нас:', type(item))
