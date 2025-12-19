import unittest
import sys
import os

# coding: utf-8

def run_all_tests():
    """
    Запускает все тесты из файлов с фигурами.
    """
    # Находим все файлы с тестами
    test_files = ['rectangle.py', 'square.py', 'triangle.py', 'circle.py']
    
    # Создаем TestLoader
    loader = unittest.TestLoader()
    
    # Загружаем тесты из каждого файла
    suites = []
    for file in test_files:
        if os.path.exists(file):
            # Импортируем модуль
            module_name = file.replace('.py', '')
            module = __import__(module_name)
            
            # Находим все тестовые классы в модуле
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, unittest.TestCase) and 
                    attr != unittest.TestCase):
                    suites.append(loader.loadTestsFromTestCase(attr))
    
    if not suites:
        print("Не найдены тесты для запуска!")
        return 1
    
    # Объединяем все тестовые наборы
    all_tests = unittest.TestSuite(suites)
    
    # Запускаем тесты с подробным выводом
    print("Запуск всех тестов...")
    print("=" * 60)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(all_tests)
    
    # Выводим статистику
    print("\n" + "=" * 60)
    print("СТАТИСТИКА ТЕСТИРОВАНИЯ:")
    print("=" * 60)
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    print("=" * 60)
    
    if result.wasSuccessful():
        print("Все тесты пройдены успешно!")
        return 0
    else:
        print("Обнаружены проблемы в тестах!")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())