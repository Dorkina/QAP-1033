from math import pi

class Rectangle:
    def __init__(self, weight, hight):
        self.weight = weight
        self.hight = hight

    def get_area(self):
        return self.weight * self.hight

class Sqare:
    def __init__(self, weight):
        self.weight = weight

    def get_area(self):
        return self.weight ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2