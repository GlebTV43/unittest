import math

def area(a, b, c):
    """
    Вычисляет площадь треугольника по формуле Герона.
    
    Параметры:
    a (int/float): длина первой стороны
    b (int/float): длина второй стороны  
    c (int/float): длина третьей стороны
    
    Возвращает:
    float: площадь треугольника
    
    Пример:
    >>> area(3, 4, 5)
    6.0
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Все стороны треугольника должны быть положительными")
    
    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника.
    
    Параметры:
    a (int/float): длина первой стороны
    b (int/float): длина второй стороны
    c (int/float): длина третьей стороны
    
    Возвращает:
    int/float: периметр треугольника
    
    Пример:
    >>> perimeter(3, 4, 5)
    12
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Все стороны треугольника должны быть положительными")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    
    return a + b + c

# ============================================
# UNIT-ТЕСТЫ для треугольника (12 тестов)
# ============================================

import unittest

class TestTriangle(unittest.TestCase):
    """Тестовый класс для проверки функций треугольника"""
    
    # ТЕСТЫ ПЛОЩАДИ
    
    def test_area_right_triangle(self):
        """Тест: площадь прямоугольного треугольника"""
        self.assertAlmostEqual(area(3, 4, 5), 6.0)
    
    def test_area_equilateral(self):
        """Тест: площадь равностороннего треугольника"""
        a = 5
        expected = (math.sqrt(3) / 4) * a * a
        self.assertAlmostEqual(area(a, a, a), expected)
    
    def test_area_zero_side(self):
        """Тест: сторона равна нулю вызывает исключение"""
        with self.assertRaises(ValueError):
            area(0, 4, 5)
    
    def test_area_triangle_inequality(self):
        """Тест: нарушение неравенства треугольника"""
        with self.assertRaises(ValueError):
            area(1, 2, 10)
    
    # ТЕСТЫ ПЕРИМЕТРА
    
    def test_perimeter_right_triangle(self):
        """Тест: периметр прямоугольного треугольника"""
        self.assertEqual(perimeter(3, 4, 5), 12)
    
    def test_perimeter_equilateral(self):
        """Тест: периметр равностороннего треугольника"""
        self.assertEqual(perimeter(5, 5, 5), 15)
    
    def test_perimeter_negative(self):
        """Тест: отрицательная сторона вызывает исключение"""
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
    
    def test_perimeter_invalid_triangle(self):
        """Тест: несуществующий треугольник вызывает исключение"""
        with self.assertRaises(ValueError):
            perimeter(2, 3, 5)  # 2 + 3 = 5
    
    # ОБЩИЕ ТЕСТЫ
    
    def test_consistency(self):
        """Тест: согласованность площади и периметра"""
        a, b, c = 6, 8, 10
        self.assertEqual(perimeter(a, b, c), a + b + c)
        p = (a + b + c) / 2
        expected_area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        self.assertAlmostEqual(area(a, b, c), expected_area)
    
    def test_commutative_property(self):
        """Тест: площадь не зависит от порядка сторон"""
        self.assertEqual(area(3, 4, 5), area(4, 5, 3))
        self.assertEqual(perimeter(3, 4, 5), perimeter(4, 5, 3))
    
    def test_float_sides(self):
        """Тест: вычисления с дробными сторонами"""
        self.assertAlmostEqual(area(2.5, 3.5, 4.5), 4.353070037)
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.5), 10.5)
    
    def test_string_input(self):
        """Тест: строковый ввод вызывает TypeError"""
        with self.assertRaises(TypeError):
            area("3", 4, 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)