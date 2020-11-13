"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    def __init__(self, ymd_str: str):

        self.__year, self.__month, self.__day = MyDate.parse_date(ymd_str)
        MyDate.validate_date(self.__year, self.__month, self.__day)

    @classmethod
    def args_to_int(cls, *args) -> list:
        """ Проверяет, что год, месяц и день являются числами или могут быть приведены к числам """
        result = []
        for value in args:
            if isinstance(value, str) or isinstance(value, int):
                try:
                    result.append(int(value))
                except ValueError:
                    raise ValueError(
                        'Дата должна задаавться набором из целых чисел или '
                        'строк, которые можно привести к целым числам')
            else:
                raise ValueError(
                    'Дата должна задаваться набором из целых чисел или '
                    'строк, которые можно привести к целым числам')
        return result

    @classmethod
    def parse_date(cls, date: str) -> list:
        seps = ['-', '.', '/']
        date_as_list = []
        for sep in seps:
            date_as_list = date.split(sep)
            if len(date_as_list) == 3:
                break
        if len(date_as_list) == 3:
            return MyDate.args_to_int(*date_as_list)
        else:
            raise ValueError(f'Неправильный формат даты. Ожидается год-месяц-день. Возможные разделители: {seps}')

    @staticmethod
    def validate_date(year: int, month: int, day: int):
        if year < 0:
            raise ValueError('Год не может быть отрицательным')

        if month > 12 or month < 0:
            raise ValueError('Неправильное значение для месяца')

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and year % 4 == 0:
            month_days[1] = 29
        if day < 0 or day > month_days[month - 1]:
            raise ValueError('Неправильное значение для дня')

        return year, month, day

    @property
    def dmy(self, sep='-'):
        return f'{self.__day:02d}{sep}{self.__month:02d}{sep}{self.__year}'


# main
if __name__ == '__main__':
    test_data = [['2009-05-23', '23-05-2009'], ['2008-2-29', '29-02-2008'], 'aw-10-10', 'asdasd123', '-2009/05/31',
                 '2020-18-10', '2009-2-29', '2020-10-45']

    test_date = MyDate(test_data[0][0]).dmy
    assert test_date == test_data[0][1]
    print(f'{test_data[0][0]}\t\t{test_date}')

    test_date = MyDate(test_data[1][0]).dmy
    assert test_date == test_data[1][1]
    print(f'{test_data[1][0]}\t\t{test_date}')

    for test_date in test_data[2:]:
        try:
            print(MyDate(test_date).dmy)
        except ValueError as e:
            print(test_date, e, sep='\t\t')
