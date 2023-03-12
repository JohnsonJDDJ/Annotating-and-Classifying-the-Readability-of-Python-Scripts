"""
Задание №5

Дорабатываем класс прямоугольник из прошлого семинара.

Добавьте возможность сложения и вычитания.

При этом должен создаваться новый экземпляр прямоугольника.

Складываем и вычитаем периметры, а не длину и ширину.

При вычитании не допускайте отрицательных значений.
"""
"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        # self.width = width if width else length
        self.width = width if width is not None else length  # 35:37
        # self.width = length if width is None else width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def __add__(self, other):
        return self.perimeter() + other.perimeter()

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self.perimeter, other.perimeter = other.perimeter, self.perimeter
        return self.perimeter() - other.perimeter()


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.perimeter())
    r2 = Rectangle(4, 5)
    print(r2.perimeter())
    r3 = r1 + r2

    print(f'{r1 = }')
    print(f'{r3 = }')
    # print(r1 + r2)
    # print(r1 - r2)
"""
8
18
r1 = <__main__.Rectangle object at 0x7f1fec69ffd0>
r3 = 26

Process finished with exit code 0
"""
# 1:33:40