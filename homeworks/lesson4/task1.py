"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours, hour_wage, bonus = argv

try:
    print(f'Скрипт {script_name} рассчитал заробботную плату {int(hours) * int(hour_wage) + int(bonus)}')
except ValueError:
    print(f'Скрипт {script_name} ожидает три целых числа в качестве параметров')
