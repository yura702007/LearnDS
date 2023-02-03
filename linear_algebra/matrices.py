from typing import Tuple, List

Matrix = List[List[float]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Возвращает (число строк А, число столбцов А)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # Число элементов в первой строке
    return num_rows, num_cols


def main():
    A = [[1, 2, 3],
         [4, 5, 6]]
    assert shape(A) == (2, 3)  # 2 строки, 3 столбца
    print(shape(A))


if __name__ == '__main__':
    main()
