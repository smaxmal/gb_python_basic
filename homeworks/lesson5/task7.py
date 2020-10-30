"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from json import dump
from homeworks.lesson5.my_functions import my_round


def read_file():
    """ read_file() -> str

    Открывает и загружает файл в текстовом режиме. Возвращает его содержимое
    """
    try:
        with open('test_data/task7_input', encoding='UTF-8') as file_in:
            return file_in.read()

    except IOError as io:
        raise IOError(f'Что-то пошло не так с файлом: {str(io)}')


def parse_content(file_data: str):
    """ parse_content(file_data: str) -> generator object


    :param file_data: содержимое файла, прочитанное одной строкой
    :return: генератор пар значений: название фирмы и прибыль
    """

    if type(file_data) is not str:
        raise TypeError('Параметр file_data в функции parse_content должен быть строкой')

    file_data = file_data.splitlines(False)
    try:
        for line in file_data:
            company_out, _, revenue, expenses = line.split(' ')
            profit_out = int(revenue) - int(expenses)

            yield company_out, profit_out

    except ValueError:
        raise ValueError('Строка файла содержит неверное число полей (должно быть 4)')

    except TypeError:
        raise TypeError('Прибыль и убытки должны быть заданы числом')


def file_write_json(file_data):
    """  file_write_json(file_date: Any) -> None

    Записывает переданные данные в json файл
    """

    try:
        with open('test_data/task7_output.json', 'w', encoding='UTF-8') as file_out:
            dump(file_data, file_out, ensure_ascii=False)

    except IOError as io:
        raise IOError(f'Что-то пошло не так с файлом: {str(io)}')


# main
content = read_file()
company_count = 0
total_profit = 0
data_output_list = []
company_dict = {}
try:
    for company_name, profit in parse_content(content):
        company_dict[company_name] = profit
        if profit > 0:
            company_count += 1
            total_profit += profit

    if len(company_dict) > 0:
        data_output_list.append(company_dict)

        average_profit = 0
        if company_count > 0:
            average_profit = my_round(total_profit / company_count, 2)

        data_output_list.append({'average_profit': average_profit})
        file_write_json(data_output_list)
        print('JSON файл успешно создан')
    else:
        print('Исходный файл пустой')

except TypeError as te:
    print(str(te))
