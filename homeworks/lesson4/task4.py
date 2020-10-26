"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


def modified_list(src_list):
    """ modified_ist (src_list) -> generator object

    Функция принимает список и возвращает генератор неповторяющихся значений входного списка

    :param src_list: исходный список
    :return: генератор
    """
    while True:
        first_time = True
        try:
            item = src_list[0]
        except IndexError:
            # дошли до конца списка
            break

        src_list.remove(item)
        while True:
            try:
                # пытаемся удалить дупликат
                src_list.remove(item)
                first_time = False
            except ValueError:
                if first_time:
                    # дупликата нет и не было
                    yield item
                break


source_list = [68, 2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 68, 75]
print([item for item in modified_list(source_list)])
