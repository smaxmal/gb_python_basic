"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""

from itertools import chain


class Matrix:
    def __init__(self, matrix_in: list):
        self.__matrix = matrix_in

    def __str__(self):
        # наибольшая длина числа из матрицы (либо наибольшее положительное число, либо наименьшее отрицательное)
        sorted_list = sorted(chain.from_iterable(self.__matrix))
        max_len = max([len(str(sorted_list[0])), len(str(sorted_list[-1]))]) + 1

        result = ''
        for row in self.__matrix:
            idx = 0
            for col in row:
                if idx > 0:
                    result = result + ' '
                result += str(col).center(max_len)
            result += '\n'
        return result

    @property
    def list(self):
        return self.__matrix

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Оператор сложения работает только с объектами класса Matrix')

        result_row = []
        for row1, row2 in zip(self.__matrix, other.list):
            result_col = []
            for col1, col2 in zip(row1, row2):
                result_col.append(col1 + col2)
            result_row.append(result_col)

        return Matrix(result_row)


# main
matrix = Matrix([[10, 20, 30], [5, -6, 8], [0, 12, 56]])
other_matrix = Matrix([[-3, 12, 45], [77, -4, 98], [3, 0, 17]])
matrix_sum = matrix + other_matrix
print(matrix)
print(other_matrix)
print(matrix_sum)
