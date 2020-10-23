"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def my_sum(iterable, terminate_str='q'):
    """
    Суммирует числа, переданные в виде спсика или кортежа
    :param iterable: список или кортеж чисел
    :param terminate_str: строка, используемая для заверщения последовательности
    :return: сумма переданных чисел, True или False, если нашли спец символ
    """
    if type(iterable) is not list and type(iterable) is not tuple:
        raise TypeError('my_sum принимает только списки или кортежи')

    iter_sum = 0
    user_terminated_entry = False
    for item in iterable:
        try:
            if str(item) == terminate_str:
                user_terminated_entry = True
                break
            iter_sum += int(item)
        except ValueError:
            raise ValueError('Надо было вводить число')
    return iter_sum, user_terminated_entry


# main
total_sum = 0
input_list = []
while True:
    try:
        input_list = input('Введите набор из чисел, разделенных пробелом (q для выхода)\n>>>').split(' ')
        if len(input_list) == 0:
            print('Введите хотя бы что-то')
            continue

        current_sum, terminate_entry = my_sum(input_list)
        total_sum += current_sum
        print(f'Полная сумма сейчас: {total_sum}')
        if terminate_entry:
            break
    except ValueError as v:
        print(str(v))
        break
    except TypeError as t:
        print(str(t))
        break
