from math import sqrt


message = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Печатает квадратный корень из числа."""
    if your_number <= 0:

        return

    Y_N = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из'
          f' введённого вами числа. Это будет: {Y_N}')


print(message)
22
calc(25)
