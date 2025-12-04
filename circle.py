import math

def area(r):
    """
    Вычисляет площадь круга.
    
    Параметры:
    r (int/float): радиус круга
    
    Возвращает:
    float: площадь круга
    
    Пример:
    >>> area(1)
    3.141592653589793
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r

def perimeter(r):
    """
    Вычисляет длину окружности.
    
    Параметры:
    r (int/float): радиус окружности
    
    Возвращает:
    float: длина окружности
    
    Пример:
    >>> perimeter(1)
    6.283185307179586
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r


import unittest

class TestCircle(unittest.TestCase):
    """Тестовый класс для проверки функций круга"""
    
    # ТЕСТЫ ПЛОЩАДИ
    
    def test_area_radius_one(self):
        """Тест: площадь при радиусе 1"""
        self.assertAlmostEqual(area(1), math.pi)
    
    def test_area_zero_radius(self):
        """Тест: площадь при нулевом радиусе"""
        self.assertEqual(area(0), 0)
    
    def test_area_positive(self):
        """Тест: площадь при положительном радиусе"""
        self.assertAlmostEqual(area(2), math.pi * 4)
    
    def test_area_negative(self):
        """Тест: отрицательный радиус вызывает исключение"""
        with self.assertRaises(ValueError):
            area(-1)
    
    # ТЕСТЫ ДЛИНЫ ОКРУЖНОСТИ
    
    def test_perimeter_radius_one(self):
        """Тест: длина окружности при радиусе 1"""
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
    
    def test_perimeter_zero(self):
        """Тест: длина окружности при нулевом радиусе"""
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_positive(self):
        """Тест: длина окружности при положительном радиусе"""
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)
    
    def test_perimeter_negative(self):
        """Тест: отрицательный радиус вызывает исключение"""
        with self.assertRaises(ValueError):
            perimeter(-2)
    
    # ОБЩИЕ ТЕСТЫ
    
    def test_consistency(self):
        """Тест: согласованность площади и длины окружности"""
        r = 5
        self.assertAlmostEqual(area(r), math.pi * r * r)
        self.assertAlmostEqual(perimeter(r), 2 * math.pi * r)
    
    def test_relationship(self):
        """Тест: связь между площадью и длиной окружности"""
        r = 4
        # Проверяем: S = C²/(4π)
        C = perimeter(r)
        S = area(r)
        self.assertAlmostEqual(S, (C * C) / (4 * math.pi))

if __name__ == "__main__":
    unittest.main(verbosity=2)