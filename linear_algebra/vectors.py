from typing import List

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

    print(add(vector_1, vector_2))
    print(subtract(vector_1, vector_2))


if __name__ == '__main__':
    main()
