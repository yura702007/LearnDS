from matplotlib import pyplot as plt


# Линейный график

def draw_trends(n=9):
    xs = [i for i in range(n)]
    variance = [2 ** x for x in xs]  # Дисперсия
    bias_squared = variance[-1::-1]  # Квадрат смещения
    total_error = [x + y for x, y in zip(variance, bias_squared)]  # Суммарная ошибка

    # Метод plt.plot можно вызвать много раз,
    # что бы показать много графиков на одной и той же диаграмме

    # зелёная сплошная линия
    plt.plot(xs, variance, 'g-', label='дисперсия')
    # красная штрихпунктирная линия
    plt.plot(xs, bias_squared, 'r-.', label='смещение^2')
    # синяя пунктирная линия
    plt.plot(xs, total_error, 'b:', label='суммарная ошибка')

    # Если для каждой линии задано название label,
    # то легенда будет показана автоматически,
    # loc=9 означает "наверху посредине"
    plt.legend(loc=9)
    plt.xlabel('Сложность модели')
    plt.title('Компромисс между смещением и дисперсией')

    plt.show()


def main():
    draw_trends()


if __name__ == '__main__':
    main()
