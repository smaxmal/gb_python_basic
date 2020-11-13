"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class MyZeroDivisionException(ZeroDivisionError):
    def __init__(self, msg):
        super().__init__(msg)


class ThatIsEnoughException(Exception):
    pass


class MyValueError(TypeError):
    def __init__(self, msg):
        super().__init__(msg)


def parse_input(value: str) -> float:
    if value == 'q':
        raise ThatIsEnoughException

    try:
        input_float = float(value)
    except ValueError:
        raise MyValueError('Это не число')

    if input_float == 0:
        raise MyZeroDivisionException("Давайте не будем делить на ноль")

    return input_float


# main
if __name__ == '__main__':
    while True:
        input_str = input('ВВедите число или "q" для выхода\n>>>')
        try:
            print(1 / parse_input(input_str))
        except MyValueError as e:
            print(e)
        except MyZeroDivisionException as e:
            print(e)
        except ThatIsEnoughException:
            break
