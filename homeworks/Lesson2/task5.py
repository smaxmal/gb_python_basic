"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
rate_list = [18, 18, 12, 10, 7, 5, 5, 2]
while True:
    new_rate = input('Введите рейтинг (натуральное число, начиная с 1) или 0 выхода\n>>>')
    if not new_rate.isdigit():
        print(f'Это не натуральное число')
    else:
        new_rate = int(new_rate)
        if not new_rate:
            break

        # ищем такое же значение
        min_index = 0
        max_index = len(rate_list) - 1
        index = len(rate_list) // 2
        while rate_list[index] != new_rate and min_index <= max_index:
            if new_rate > rate_list[index]:
                max_index = index - 1
            else:
                min_index = index + 1
            index = (min_index + max_index) // 2

        # если нашли, ищем последнее такое же
        if min_index < max_index:
            while index + 1 < len(rate_list) and rate_list[index + 1] == new_rate:
                index += 1

        rate_list = rate_list[0:index + 1] + [new_rate] + rate_list[index + 1:]
        print(f'Обновленный список: {rate_list}\n')
