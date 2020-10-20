"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
our_list = []
confirm_in = ''

print('Начнем ввод списка')
while True:
    confirm_in = input(f'элемент списка № {len(our_list) + 1} (q - для выхода)\n>>>')
    if confirm_in != 'q':
        our_list.append(confirm_in)
    else:
        break

print('Вот такой список получился:')
for item in our_list:
    print(f'{item}')

print('Теперь меняем местами элементы с индексами 0 и 1, 2 и 3 и т.д.:')
item_num = 0
for item in our_list:
    if item_num & 1 == 1:
        our_list[item_num], our_list[item_num - 1] = our_list[item_num - 1], our_list[item_num]
    item_num += 1

for item in our_list:
    print(f'{item}')
