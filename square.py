def area(a):
    """
    Вычисляет площадь квадрата.
    
    Параметры:
    a (int/float): длина стороны квадрата
    
    Возвращает:
    int/float: площадь квадрата
    
    Пример:
    >>> area(4)
    16
    """
    if a < 0:
        raise ValueError("Сторона квадрата должна быть неотрицательной")
    return a * a

def perimeter(a):
    """
    Вычисляет периметр квадрата.
    
    Параметры:
    a (int/float): длина стороны квадрата
    
    Возвращает:
    int/float: периметр квадрата
    
    Пример:
    >>> perimeter(4)
    16
    """
    if a < 0:
        raise ValueError("Сторона квадрата должна быть неотрицательной")
    return 4 * a

import unittest

class TestSquare(unittest.TestCase):
    """Тестовый класс для проверки функций квадрата"""
    
    # ТЕСТЫ ПЛОЩАДИ
    
    def test_area_normal(self):
        """Тест: площадь с положительным целым числом"""
        self.assertEqual(area(5), 25)
    
    def test_area_zero(self):
        """Тест: площадь при нулевой стороне"""
        self.assertEqual(area(0), 0)
    
    def test_area_float(self):
        """Тест: площадь с дробным числом"""
        self.assertAlmostEqual(area(2.5), 6.25)
    
    def test_area_negative(self):
        """Тест: отрицательная сторона вызывает исключение"""
        with self.assertRaises(ValueError):
            area(-5)
    
    # ТЕСТЫ ПЕРИМЕТРА
    
    def test_perimeter_normal(self):
        """Тест: периметр с положительным целым числом"""
        self.assertEqual(perimeter(5), 20)
    
    def test_perimeter_one(self):
        """Тест: периметр при стороне равной 1"""
        self.assertEqual(perimeter(1), 4)
    
    def test_perimeter_float(self):
        """Тест: периметр с дробным числом"""
        self.assertAlmostEqual(perimeter(2.5), 10.0)
    
    def test_perimeter_negative(self):
        """Тест: периметр с отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-5)
    
    # ОБЩИЕ ТЕСТЫ
    
    def test_consistency(self):
        """Тест: согласованность площади и периметра"""
        side = 6
        self.assertEqual(area(side), side * side)
        self.assertEqual(perimeter(side), 4 * side)
    
    def test_string_input(self):
        """Тест: строковый ввод вызывает TypeError"""
        with self.assertRaises(TypeError):
            area("5")

if __name__ == "__main__":
    unittest.main(verbosity=2)