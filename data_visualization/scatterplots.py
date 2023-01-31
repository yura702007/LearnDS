from matplotlib import pyplot as plt


# Диаграммы рассеяния

def dependency_on_friends():
    """
    Связь между числом друзей пользователей и
    количеством времени,
    которое они проводят на сайте
    :return:
    """
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]  # друзья
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]  # минуты
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # метки

    plt.scatter(friends, minutes)

    # Назначить метку для каждой точки
    for label, friend, minute in zip(labels, friends, minutes):
        plt.annotate(
            label,
            xy=(friend, minute),  # задать метку
            xytext=(5, -5),  # и немного сместить её
            textcoords='offset points'
        )

    plt.title('Число минут против числа друзей')
    plt.xlabel('Число друзей')
    plt.ylabel('Число минут, проводимых на сайте ежедневно')

    plt.show()


def main():
    dependency_on_friends()


if __name__ == '__main__':
    main()
