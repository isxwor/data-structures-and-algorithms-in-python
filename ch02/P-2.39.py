''' P-2.39
Develop an inheritance hierarchy based upon a Polygon class that has
abstract methods area() and perimeter(). Implement classes Triangle,
Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
class, with the obvious meanings for the area() and perimeter() methods.
Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle,
and Square, that have the appropriate inheritance relationships. Finally,
write a simple program that allows users to create polygons of the
various types and input their geometric dimensions, and the program then
outputs their area and perimeter. For extra effort, allow users to input
polygons by specifying their vertex coordinates and be able to test if two
such polygons are similar.
'''

from abc import ABCMeta, abstractmethod
import math


# TODO:
# allow users to input polygons by specifying their vertex coordinates
# and be able to test if two such polygons are similar

class Polygon(metaclass=ABCMeta):
    ''' supports regular polygons only '''
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Polygon):
    def __init__(self, *sides):
        if len(sides) < 3:
            raise TypeError(
                f'missing {3-len(sides)} positional arguments'
            )
        elif len(sides) > 3:
            raise TypeError(
                f'Triangle takes 3 positional arguments but {len(sides)} were given'
            )
        self._sides = sides
    
    def area(self):
        ''' Calculating area of a triangle using Heron's formula '''
        s = self.perimeter() / 2
        result = s
        for side in self._sides:
            result *= (s - side)
        return round(math.sqrt(result), 2)
    
    def perimeter(self):
        return sum(self._sides)


class IsoscelesTriangle(Triangle):
    def __init__(self, side, base):
        sides = [side]*2 + [base] # side, side, base
        super().__init__(*sides)


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        sides = [side] * 3
        super().__init__(*sides)


class Quadrilateral(Polygon):
    ''' provides defination for perimeter method only
    
    depends on subclass for appropriate defination for area method '''
    def __init__(self, *sides):
        if len(sides) < 4:
            raise TypeError(
                f'missing {4-len(sides)} positional arguments'
            )
        elif len(sides) > 4:
            raise TypeError(
                f'Quadrilateral takes 4 positional arguments but {len(sides)} were given'
            )
        self._sides = sides
    
    def perimeter(self):
        return sum(self._sides)


class Rectangle(Quadrilateral):
    def __init__(self, length, breadth):
        sides = [length]*2 + [breadth]*2  # length, length, breadth, breadth
        super().__init__(*sides)
    
    def area(self):
        result = self._sides[0] * self._sides[-1]
        return round(result, 2)


class Square(Quadrilateral):
    def __init__(self, side):
        sides = [side] * 4
        super().__init__(*sides)
    
    def area(self):
        result = self._sides[0] ** 2
        return round(result, 2)


class Pentagon(Polygon):
    def __init__(self, side):
        self._side = side
    
    def area(self):
        rad = 54 * (math.pi/180)  # math.tan() takes argument in radians
        result = (5 * pow(self._side, 2) * math.tan(rad)) / 4
        return round(result, 2)
    
    def perimeter(self):
        return (5 * self._side)


class Hexagon(Polygon):
    def __init__(self, side):
        self._side = side
    
    def area(self):
        result = ((3 * math.sqrt(3)) / 2) * pow(self._side, 2)
        return round(result, 2)
    
    def perimeter(self):
        return (6 * self._side)


class Octagon(Polygon):
    def __init__(self, side):
        self._side = side
    
    def area(self):
        result = 2 * (1 + math.sqrt(2)) * pow(self._side, 2)
        return round(result, 2)
    
    def perimeter(self):
        return (8 * self._side)


if __name__ == '__main__':
    # -------- Tests -------- #
    tri = Triangle(12, 10, 8)
    itr = IsoscelesTriangle(12, 10)
    eqt = EquilateralTriangle(8)
    rec = Rectangle(12, 10)
    sqr = Square(10)
    pen = Pentagon(12)
    hex = Hexagon(10)
    oct = Octagon(14)
    
    print('# Triangle')
    print(f'Area: {tri.area()}\nPerimeter: {tri.perimeter()}\n')
    
    print('# Isoceles Triangle')
    print(f'Area: {itr.area()}\nPerimeter: {itr.perimeter()}\n')
    
    print('# Equilateral Triangle')
    print(f'Area: {eqt.area()}\nPerimeter: {eqt.perimeter()}\n')
    
    print('# Rectangle')
    print(f'Area: {rec.area()}\nPerimeter: {rec.perimeter()}\n')
    
    print('# Square')
    print(f'Area: {sqr.area()}\nPerimeter: {sqr.perimeter()}\n')
    
    print('# Pentagon')
    print(f'Area: {pen.area()}\nPerimeter: {pen.perimeter()}\n')
    
    print('# Hexagon')
    print(f'Area: {hex.area()}\nPerimeter: {hex.perimeter()}\n')
    
    print('# Octagon')
    print(f'Area: {oct.area()}\nPerimeter: {oct.perimeter()}\n')
