from math import pi

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# area calculation method
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

# area calculation method
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

# area calculation method
    def get_area_circle(self):
        return round(self.r ** 2 * pi, 2)