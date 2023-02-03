from typing import List
import math

# Инициализация класса Вектор
Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Сложение векторов"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'
    return [sum(elem) for elem in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Разность векторов"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'
    return [a - b for a, b in zip(v, w)]


def vectors_sum(vectors: List[Vector]) -> Vector:
    """Суммирует все соответствующие элементы"""
    # Проверить, что векторы не пустые
    assert vectors, 'Векторы не предоставлены'

    # Проверить, что все векторы одинакового размера
    length_elem = len(vectors[0])
    assert all(len(v) == length_elem for v in vectors), 'разные размеры'

    return [
        sum(vector[i] for vector in vectors)
        for i in range(length_elem)
    ]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Умножает каждый элемент на c"""
    return [c * w for w in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Вычисляет покомпонентное среднее арифметическое"""
    n = len(vectors)
    return scalar_multiply(1 / n, vectors_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    """Вычисляет v_1 * w_1 + v_2 * w_2 + ... + v_n * w_n"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'
    return sum(i * j for i, j in zip(v, w))


def sum_of_squares_vector(v: Vector) -> float:
    """Вычисляет v_1 * v_1 + v_2 * v_2 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude_vector(v: Vector) -> float:
    """Возвращает длину (магнитуду) вектора"""
    # math.sqrt() - функция квадратного корня
    return math.sqrt(sum_of_squares_vector(v))



def main():
    # Создание вектора
    height_weight_age = [
        175,  # Сантиметры
        68,  # Килограммы
        40  # Годы
    ]
    grades = [
        85,  # Экзамен 1
        90,  # Экзамен 2
        73,  # Экзамен 3
        68  # Экзамен 4
    ]

    vector_1 = [24, 15, 42]
    vector_2 = [12, 36, 65]
    vector_3 = [21, 12, 34]

    print(add(vector_1, vector_2))
    print(subtract(vector_1, vector_2))
    print(vectors_sum([vector_1, vector_2, vector_3]))
    print(scalar_multiply(2, vector_1))
    print(vector_mean([vector_1, vector_2, vector_3]))
    print(dot(vector_1, vector_2))
    print(sum_of_squares_vector(vector_1))
    print(magnitude_vector(vector_1))


if __name__ == '__main__':
    main()
