"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

try:
    with open('test_data/task1_output', 'w', encoding='UTF-8') as file_out:
        print('Введите несколько строк текста. Для выхода, в начале новой строки нажмите enter после приглашения')
        while True:
            input_str = input('>>>')
            if len(input_str) == 0:
                break
            input_str += '\n'
            file_out.write(input_str)
except IOError as e:
    print(f'Что-то пошло не так с файлом: {str(e)}')
