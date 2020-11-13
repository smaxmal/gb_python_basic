"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, real: float, imaginary: float):
        try:
            self.__real = real
            self.__imaginary = imaginary
        except ValueError:
            raise ValueError('Действительная и мнимая часть комплексного числа должна задаваться '
                             'действильчислами числами или строками, которые можно к ним привести')

    @property
    def real_part(self):
        return self.__real

    @property
    def img_part(self):
        return self.__imaginary

    def __add__(self, other):
        if not isinstance(other, ComplexNum):
            try:
                real = float(other)
            except ValueError:
                raise ValueError('Операция сложения возможно только с комплексным числом или числом, которое'
                                 'можно к нему преобразовать')
            return ComplexNum(self.__real + real, self.__imaginary)
        else:
            return ComplexNum(self.__real + other.real_part, self.__imaginary + other.img_part)

    def __sub__(self, other):
        if not isinstance(other, ComplexNum):
            try:
                real = float(other)
            except ValueError:
                raise ValueError('Операция вычитания возможно только с комплексным числом или числом, которое'
                                 'можно к нему преобразовать')
            return ComplexNum(self.__real - real, self.__imaginary)
        else:
            return ComplexNum(self.__real - other.real_part, self.__imaginary - other.img_part)

    def __str__(self):
        sign = ' + '
        if self.__imaginary < 0:
            sign = ' - '
        abs_img = abs(self.__imaginary)
        img_str = f'{sign}{str(abs_img)}i'
        if abs_img == 1:
            img_str = f'{sign}i'
        if abs_img == 0:
            img_str = ''
        return f'{self.__real}{img_str}'


# main
if __name__ == '__main__':
    test_data = (((2, 1), (-3, -4), (56, 0)), '2 + i', '-3 + 4i', '56', '-1 - 3i', '57 + 3i')
    complex_1 = ComplexNum(*test_data[0][0])
    complex_2 = ComplexNum(*test_data[0][1])
    complex_3 = ComplexNum(*test_data[0][2])
    complex_4 = complex_1 + complex_2
    complex_5 = complex_3 - complex_4
    assert str(complex_1), test_data[1]
    assert str(complex_1), test_data[2]
    assert str(complex_1), test_data[3]
    assert str(complex_4), test_data[4]
    assert str(complex_5), test_data[5]
    print(complex_1, complex_2, complex_3, sep='\n')
    print(f'({complex_1}) + ({complex_2}) = {complex_4}')
    print(f'({complex_3}) - ({complex_4}) = {complex_5}')
