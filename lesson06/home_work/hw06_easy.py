# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

# class Triangle:
#     def __init__(self, A1, A2, A3):
#         self.A1 = A1
#         self.A2 = A2
#         self.A3 = A3
#         self.d1 = int(math.sqrt((self.A2[0] - self.A1[0]) ** 2 + (self.A2[1] - self.A1[1]) ** 2))
#         self.d2 = int(math.sqrt((self.A3[0] - self.A2[0]) ** 2 + (self.A3[1] - self.A2[1]) ** 2))
#         self.d3 = int(math.sqrt((self.A1[0] - self.A3[0]) ** 2 + (self.A1[1] - self.A3[1]) ** 2))
#     @property
#     def perimeter(self):
#         return self.d1 + self.d2 + self.d3
#
#     @property
#     def area(self):
#         sp = self.perimeter/2
#         return math.sqrt(sp*(sp - self.d1)*(sp - self.d2)*(sp - self.d3))
#
#     def height(self, side):
#         return 2 * self.area / side
#
# triangle1 = Triangle((24, 7), (46, 45), (36, 17))
# print(triangle1.height(triangle1.d1))





# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Equilateral_trapezoid:
    def __init__(self, A1, A2, A3, A4):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.side1 = int(math.sqrt((self.A2[0] - self.A1[0]) ** 2 + (self.A2[1] - self.A1[1]) ** 2))
        self.side2 = int(math.sqrt((self.A3[0] - self.A2[0]) ** 2 + (self.A3[1] - self.A2[1]) ** 2))
        self.side3 = int(math.sqrt((self.A4[0] - self.A3[0]) ** 2 + (self.A4[1] - self.A3[1]) ** 2))
        self.side4 = int(math.sqrt((self.A1[0] - self.A4[0]) ** 2 + (self.A1[1] - self.A4[1]) ** 2))
    def equal(self):
        if self.A2[0] >= self.A3[0]:
            self.A2, self.A3 = self.A3, self.A2
        if self.A1[0] >= self.A4[0]:
            self.A1, self.A4 = self.A4, self.A1
        self.anglekf1 = (self.A3[1] - self.A2[1])/(self.A3[0] - self.A2[0])
        self.anglekf2 = (self.A4[1] - self.A1[1])/(self.A4[0] - self.A1[0])
        if self.A1[0] >= self.A2[0]:
            self.A1, self.A2 = self.A2, self.A1
        if self.A4[0] >= self.A3[0]:
            self.A4, self.A3 = self.A3, self.A4
        self.anglekf3 = (self.A2[1] - self.A1[1]) / (self.A2[0] - self.A1[0])
        self.anglekf4 = (self.A3[1] - self.A4[1]) / (self.A3[0] - self.A4[0])
        if self.anglekf1 == self.anglekf2 or self.anglekf3 == self.anglekf4:
            print("Фигура является трапецией")
            if self.side1 == self.side3 or self.side2 == self.side4:
                print("Фигура является равнобочной трапецией")
        else:
            print("Фигура не является трапецией")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

trapezoid1 = Equilateral_trapezoid((12, 24), (16, 46), (25, 46), (29, 24))
print(trapezoid1.equal())


