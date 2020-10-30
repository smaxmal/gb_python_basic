"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

digits_in_words_ru = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре', 5: 'Пять', 6: 'Шесть', 7: 'Семь',
                      8: 'Восемь', 9: 'Девять', 10: 'Десять'}
lines_output = []
try:
    with open('test_data/task4_input', encoding='UTF-8') as file_in:
        for line in file_in:
            number, _, digit = line.split(' ')
            lines_output.append(f'{digits_in_words_ru[int(digit)]} - {digit}')

    with open('test_data/task4_output', 'w', encoding='UTF-8') as file_out:
        file_out.writelines(lines_output)

except IOError as io:
    print(f'Что-то пошло не так с файлом: {str(io)}')

except KeyError:
    print('В файле содержится неизвестное число')

except TypeError:
    print('Не удвлось разспознать число')
