"""
Сравнение экземпляров класса

Python поддерживает определение шести основных операций
сравнения экземпляров
__eq__    - равно, ==
__ne__    - не равно, !=
__gt__    - больше, >
__ge__    - не больше, меньше или равно, <=
__lt__    - меньше, <
__le__    - не меньше, больше или равно, >=
"""
from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

    def __hash__(self):
        """Пытаемся вычислить хэш от нашего экземпляра"""
        return hash((self.a, self.b, self.c))


def main():
    triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
                    Triangle(3, 5, 3)}
    print(triangle_set)
    print(', '.join(f'{item.area():.3f}' for item in triangle_set))
    print(', '.join(f'{item.__hash__()}' for item in triangle_set))


if __name__ == '__main__':
    main()
"""
{Triangle(4, 4, 4), Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(3, 5, 3)}
6.928, 6.000, 4.684, 4.146
5958266269407395088, 4003026094496801395, 7248620568795758028, -7050955881463073020

Process finished with exit code 0
"""
# 01:31:57
# 01:28:28 - обязательно для изучения !!!