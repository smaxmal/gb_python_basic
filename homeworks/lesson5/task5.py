"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randrange
import homeworks.lesson5.my_functions as myf

try:
    with open('test_data/task5_output', 'w') as file_out:
        for idx in myf.my_range_int(1, 10):
            file_out.write(str(randrange(1, 100)))
            if idx < 9:
                file_out.write(' ')

    with open('test_data/task5_output') as file_in:
        content = file_in.read().split(' ')

    print(f'Сумма чисел: {myf.my_sum(content)}')

except IOError as io:
    print(f'Что-то пошло не так с файлом: {str(io)}')

except TypeError:
    print('Не удвлось разспознать число')
