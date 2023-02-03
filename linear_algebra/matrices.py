from typing import Tuple, List, Callable
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


def get_column(A: Matrix, j: int) -> Vector:
    """Возвращает j-ый столбец как тип Vector"""
    return [i[j] for i in A]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Возвращает матрицу num_rows * num_cols,
    чей (i, j) элемент является функцией entry_fn(i, i)
    """
    return [[entry_fn(i, j)  # создать список с учётом i
             for j in range(num_cols)]  # [entry(i, 0)...]
            for i in range(num_rows)]  # создать один список для каждого i


def main():
    A = [[1, 2, 3],
         [4, 5, 6]]
    assert shape(A) == (2, 3)  # 2 строки, 3 столбца
    print(shape(A))
    assert get_row(A, 1) == [4, 5, 6]
    print(get_row(A, 1))
    assert get_column(A, 2) == [3, 6]
    print(get_column(A, 2))
    assert make_matrix(2, 2, lambda i, j: 1) == [[1, 1], [1, 1]]
    print(make_matrix(2, 3, lambda i, j: 42))


if __name__ == '__main__':
    main()
