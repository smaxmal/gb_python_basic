"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

import itertools as it
from sys import argv
from time import sleep

script_name, script_num, param1 = argv

try:
    param1 = int(param1)

    predefined_list = [68, 2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 68, 75]
    idx = 0
    if script_num == '1':
        for next_num in it.count(param1):
            sleep(1)
            print(next_num)
            if next_num == param1 + 10:
                break

    elif script_num == '2':
        if param1 > 0:
            for next_num in it.cycle(predefined_list):
                if idx >= param1:
                    break
                sleep(1)
                print(next_num)
                idx += 1
        else:
            print('Для cycle второй параметр должен быть положительным целым числом')
    else:
        print('Введите два параметра:\n1 - номер скрипта (1 - для count, 2 - для cycle)\n2 - стартовое значение '
              'для count или число итераций для cycle')

except TypeError:
    print('второй параметр должен быть целым числом')
