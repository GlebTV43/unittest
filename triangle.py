import unittest

def area(a, h):
    '''
    Принимает a - длину стороны треугольника, h - длина высоты к соответствующей стороне,
    возвращает - площадь треугольника.
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Принимает : 
    a, b, c - длины сторон треугольника

    Возвращает: 
    Периметр этого треугольника.
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
