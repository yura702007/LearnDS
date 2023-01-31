from matplotlib import pyplot as plt
from collections import Counter


# Столбчатые графики


def counter_oscars():
    """
    Подсчёт количества оскаров у фильмов
    :return:
    """
    movies = ["Энни Холл", "Бен-Гур", "Касабланка", "Ганд", "Вестсайдская история"]
    num_oscars = [5, 11, 3, 8, 10]

    # Построить столбцы с левыми Х-координатам [xs] и высотам [num_oscars]
    plt.bar(range(len(movies)), num_oscars)
    plt.title("Moи любимые фильмы")  # Добавить заголовок
    plt.ylabel('Количество наград')  # Разместить метку на оси y

    # Пометить ось x названиями фильмов в центре каждого столбца
    plt.xticks(range(len(movies)), movies)
    plt.show()


def value_distribution():
    """
    Столбчатый график распределения оценок за экзамен
    :return:
    """
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 70, 0]

    # Сгруппировать оценки подецельно,
    # но разместить 100 вместе с отметками 90 и выше
    histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

    plt.bar(
        [x + 5 for x in histogram.keys()],  # Сдвинуть столбец влево на 5
        list(histogram.values()),  # Высота столбца
        10,  # Ширина каждого столбца 10
    )

    plt.axis((-5, 105, 0, 5))  # Ось х от -5 до 105, ось у от 0 до 5
    plt.xticks([10 * x for x in range(11)])  # Метки по оси х 0, 10, ..., 100
    plt.xlabel('Дециль')
    plt.ylabel('Число студентов')
    plt.title('Распределение оценок за экзамен №1')

    plt.show()


def main():
    counter_oscars()
    value_distribution()


if __name__ == '__main__':
    main()
