"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
from homeworks.lesson4.my_functions import my_range_int

print([item for item in my_range_int(20, 240) if item % 20 == 0 or item % 21 == 0])
