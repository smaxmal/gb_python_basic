"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.
"""
name = 'Гость'
surname = 'Незваный'
age = 18
city = 'Далёкий'
street = 'где-то там'
house = 1
apartment = 1

print(f'Добрый день, гость. Сейчас вы зарегистрированы как пользователь {name} {surname}, возраст: {age},',
      f'проживающий по адресу: г. {city}, улица {street}, дом {house}, кв. {apartment}\n', )

confirm = input('Хотите обновить данные (д/н)? >>>: ')
if confirm == 'д':
    name = input('Ваше имя?\n>>>: ')
    surname = input('ваша фамилия?\n>>>: ')
    city = input('город?\n>>>: ')
    street = input('улица?\n>>>: ')
    house = input('дом?\n>>>: ')
    apartment = input('квартира?\n>>>: ')
    print(f'Ваши новые данные:\n пользователь {name} {surname}, возраст: {age}, проживающий по адресу:',
          f'г. {city}, улица {street}, дом {house}, кв. {apartment}\n')
    print('До новых встреч!')
elif confirm == 'н':
    print('Не беда, можете сделать это позже.', 'До свидания!', sep='\n')
else:
    print('Будем считать, что это нет. Не беда, можете сделать это позже.', 'До свидания!', sep='\n')
