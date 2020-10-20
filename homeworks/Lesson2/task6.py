"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

property_values_dict = {}
property_types = {}
prop_num = 0
item_list = []

# Задание структуры. Для упрощения числовые характеристики будут всегда считаться целочисленными
while True:
    property_in = input(f'Введите название характеристики №{prop_num + 1} товара '
                        f'(0 - для завершения ввода), пробел, затем 1, если свойство целое число (например, цена)\n>>>')
    if property_in == '0':
        break

    prop_num += 1
    property_list = property_in.split(' ')
    if len(property_list) > 1 and len(property_list[1]) > 0:
        property_types[property_list[0]] = bool(property_list[1])
    else:
        property_types[property_list[0]] = False

# print(property_types)

if prop_num > 0:
    item_num = 1

    # цикл по товарам
    while True:

        # инициализируем новый словарь
        if len(property_values_dict) > 0:
            property_values_dict = property_values_dict.copy()
            property_values_dict.clear()

        for property_name, property_is_numeric in property_types.items():

            # пока не введем значение правильного типа или не откажемся вводить дальше
            while True:
                property_value = input(f'Товар {item_num}, Введите значение для характеристики {property_name}'
                                       f' или q для завершения\n>>>')
                if property_value == 'q':
                    break
                else:
                    if property_is_numeric:
                        if not property_value.isnumeric():
                            print(f'Характеристика {property_name} требует числового значения, попробуйте еще раз')
                            continue

                        property_values_dict[property_name] = int(property_value)
                    else:
                        property_values_dict[property_name] = property_value
                break
            # принудительный выход из цикла по свойствам
            if property_value == 'q':
                break
        # если вышли раньше, чем ввели все свойства
        if len(property_types) > len(property_values_dict):
            break

        item_list.append(tuple([item_num, property_values_dict]))
        item_num += 1

# for item in item_list:
#     print(item)

# Сбор аналитики
# Как и можно ли сделать slice из такой многоменрной структуры не очень понятно, поэтому пока делаю в лоб
analytics = {}
property_list = property_types.keys()
for property_name in property_list:
    value_list = []
    for item in item_list:
        property_dict = item[1]
        value_list.append(property_dict.get(property_name))
    analytics[property_name] = value_list

print('Аналитика:')
for property_name, property_value in analytics.items():
    print(f'{property_name} : {property_value}')
