from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("square")
        self.length = length

    def area(self):
        return self.length**2

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)

print(a)
print(a.area())


print(b)
print(b.area())
