"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

line_count = 0
try:
    with open('test_data/task2_input', encoding='UTF-8') as file_in:
        for line in file_in:
            line_count += 1
            print(f'строка: {line_count}, количество слов: {len(line.split(" "))}')

except IOError as e:
    print(f'Что-то пошло не так с файлом: {str(e)}')

print(f'Всего сток прочитано {line_count}')
