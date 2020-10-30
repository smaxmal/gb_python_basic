"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def read_file():
    """ read_file() -> list

    Открывает и загружает файл в текстовом режиме. Возвращает его содержимое в виде списка строк
    """
    try:
        with open('test_data/task6_input', encoding='UTF-8') as file_in:
            return file_in.readlines()

    except IOError as io:
        raise IOError(f'Что-то пошло не так с файлом: {str(io)}')


def parse_content(file_data: list):
    """ parse_content(file_data: list) -> generator object

    :param file_data: содержимое файла в виде списка строк
    :return: генератор пар значений: предмет и колчиство часов
    """

    for line in file_data:
        line_data = line.split(' ')
        course_name = ''
        total_hours = 0

        if len(line_data) > 1:
            try:
                # название предмета
                course_name = line_data[0]

                # убираем двоеточия после названия предмета
                if len(course_name) > 0 and course_name.endswith(':'):
                    course_name = str(course_name[:len(course_name) - 1])

                # вычленяем и суммируем числа из остальных полей
                for field in line_data[1:]:
                    number = ''
                    for char in field:
                        if char.isdigit():
                            number = number + char
                        else:
                            break
                    if len(number) > 0:
                        total_hours += int(number)

            except IndexError:
                raise IndexError('Название предмета и хотя бы один тип занятий должны присутствовать в файле')

        yield course_name, total_hours


# main
content = read_file()
course_stat = {}

try:
    for course, hours in parse_content(content):
        course_stat[course] = hours

    if len(course_stat) > 0:
        print(course_stat)
    else:
        print('Файл пустой')

except KeyError as ke:
    print(f'Ошибка парсинга файла: {str(ke)}')

except IndexError as ie:
    print(str(ie))
