"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def format_user_data(name, surname, birth_year, city, email, phone):
    return f'Имя: {name},\nФамилия: {surname},\nгод рождения: {birth_year},\nгород проживания: {city},\n' \
           f'email: {email},\nтелефон: {phone}'


# main

name_in = input('Введите имя \n>>>')
surname_in = input('Введите фамилию \n>>>')
year_in = input('Введите год рождения \n>>>')
city_in = input('Введите город проживания \n>>>')
email_in = input('Введите email \n>>>')
phone_in = input('Введите телефон \n>>>')

print(format_user_data(surname=name_in, name=surname_in, birth_year=year_in, phone=phone_in, email=email_in,
                       city=city_in))
