from typing import Tuple, List
from vectors import Vector

Matrix = List[List[float]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Возвращает (число строк А, число столбцов А)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # Число элементов в первой строке
    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """Возвращает i-ую строку как тип Vector"""
    return A[i]


def main():
    A = [[1, 2, 3],
         [4, 5, 6]]
    assert shape(A) == (2, 3)  # 2 строки, 3 столбца
    print(shape(A))
    assert get_row(A, 1) == [4, 5, 6]
    print(get_row(A, 1))


if __name__ == '__main__':
    main()
