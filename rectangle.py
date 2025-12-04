def area(a, b):
    """
    Вычисляет площадь прямоугольника.
    
    Параметры:
    a (int/float): длина первой стороны
    b (int/float): длина второй стороны
    
    Возвращает:
    int/float: площадь прямоугольника
    
    Пример:
    >>> area(5, 3)
    15
    """
    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника должны быть неотрицательными")
    return a * b

def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника.
    
    Параметры:
    a (int/float): длина первой стороны
    b (int/float): длина второй стороны
    
    Возвращает:
    int/float: периметр прямоугольника
    
    Пример:
    >>> perimeter(5, 3)
    16
    """
    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника должны быть неотрицательными")
    return 2 * (a + b)


import unittest

class TestRectangle(unittest.TestCase):
    """Тестовый класс для проверки функций прямоугольника"""
    
    # ТЕСТЫ ПЛОЩАДИ
    
    def test_area_normal(self):
        """Тест: площадь с положительными целыми числами"""
        self.assertEqual(area(5, 3), 15)
    
    def test_area_zero_side(self):
        """Тест: площадь при нулевой стороне"""
        self.assertEqual(area(0, 10), 0)
    
    def test_area_float(self):
        """Тест: площадь с дробными числами"""
        self.assertAlmostEqual(area(2.5, 3.5), 8.75)
    
    def test_area_negative(self):
        """Тест: отрицательные стороны вызывают исключение"""
        with self.assertRaises(ValueError):
            area(-5, 3)
    
    # ТЕСТЫ ПЕРИМЕТРА
    
    def test_perimeter_normal(self):
        """Тест: периметр с положительными целыми числами"""
        self.assertEqual(perimeter(5, 3), 16)
    
    def test_perimeter_square(self):
        """Тест: периметр квадрата (частный случай)"""
        self.assertEqual(perimeter(4, 4), 16)
    
    def test_perimeter_zero(self):
        """Тест: периметр при нулевых сторонах"""
        self.assertEqual(perimeter(0, 0), 0)
    
    def test_perimeter_negative(self):
        """Тест: периметр с отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(5, -3)
    
    # ОБЩИЕ ТЕСТЫ
    
    def test_consistency(self):
        """Тест: согласованность площади и периметра"""
        a, b = 7, 4
        self.assertEqual(area(a, b), a * b)
        self.assertEqual(perimeter(a, b), 2 * (a + b))
    
    def test_string_input(self):
        """Тест: строковый ввод вызывает TypeError"""
        with self.assertRaises(TypeError):
            area("5", 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)