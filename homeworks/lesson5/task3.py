"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from homeworks.lesson5.my_functions import my_round


def read_file():
    """ read_file() -> str

    Открывает и загружает файл в текстовом режиме. Возвращает его содержимое
    """
    try:
        with open('test_data/task3_input', encoding='UTF-8') as file_in:
            return file_in.read()

    except IOError as io:
        raise IOError(f'Что-то пошло не так с файлом: {str(io)}')


def parse_content(file_data: str):
    """ parse_content(file_data: str) -> generator object

    :param file_data: содержимое файла, прочитанное одной строкой
    :return: генератор пар значений: фамилия и зарплата
    """

    if type(file_data) is not str:
        raise TypeError('Параметр file_data в функции parse_content должен быть строкой')

    file_data = file_data.splitlines(False)
    try:
        for line in file_data:
            surname_out, wage_out = line.split(' ')
            wage_out = int(wage_out)
            yield surname_out, wage_out

    except TypeError:
        raise TypeError('Данные в файле либо неполные, либо сохранены в неправильном порядке.')

    except ValueError:
        raise ValueError('Файл содержит больше или меньше эелементов данных, чем ожидается')


# main
content_in = read_file()

underpaid_list = []
total_wage = 0
headcount = 0
try:
    for surname, wage in parse_content(content_in):
        headcount += 1
        if wage < 20000:
            underpaid_list.append(surname)
        total_wage += wage

    if headcount > 0:
        print(f'Средняя зарплата: {my_round(total_wage / headcount, 2)}\n')
        print('Фамилии сотрудников с окладом менее 20 тыс.р.:')
        for surname in underpaid_list:
            print(surname)
    else:
        print('Файл пустой')

except TypeError as te:
    print(str(te))

except ValueError as ve:
    print(f'Файл пустой: {str(ve)}')
