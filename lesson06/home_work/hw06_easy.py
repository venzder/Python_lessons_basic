# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, A1, A2, A3):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.d1 = int(math.sqrt((self.A2[0] - self.A1[0]) ** 2 + (self.A2[1] - self.A1[1]) ** 2))
        self.d2 = int(math.sqrt((self.A3[0] - self.A2[0]) ** 2 + (self.A3[1] - self.A2[1]) ** 2))
        self.d3 = int(math.sqrt((self.A1[0] - self.A3[0]) ** 2 + (self.A1[1] - self.A3[1]) ** 2))
    @property
    def perimeter(self):
        return self.d1 + self.d2 + self.d3

    @property
    def area(self):
        sp = self.perimeter/2
        return math.sqrt(sp*(sp - self.d1)*(sp - self.d2)*(sp - self.d3))

    def height(self, side):
        return 2 * self.area / side

triangle1 = Triangle((24, 7), (46, 45), (36, 17))
print(triangle1.height(d1))




# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

