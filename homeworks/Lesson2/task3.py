"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
seasons = ['весна', 'лето', 'осень', 'зима']
months = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
          10: 'осень', 11: 'осень', 12: 'зима'}

month_num = input('Введите номер месяца от 1 до 12:\n>>>')
if not month_num.isdigit():
    print('Это было не число')
else:
    month_num = int(month_num)
    if month_num < 1 or month_num > 12:
        print('Не верный номер месяца')
    else:
        print(f'Решение через list: Это {seasons[month_num // 3 - 1]}')

        print(f'Решение через dict: Это {months[month_num]}')
