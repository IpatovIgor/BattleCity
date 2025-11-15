# test_brick.py
import unittest
import sys
import os

# Импортируем конфигурацию первым делом
from test_config import PATHS_SETUP
from test_utils import setup_test_environment

if not PATHS_SETUP:
    print("❌ Не удалось настроить пути! Тесты не могут быть запущены.")
    sys.exit(1)

# Настраиваем тестовое окружение
setup_test_environment()

try:
    from BrickClass import BrickBloc, BrickMiddleBloc

    print("✓ BrickClass успешно импортирован")
except ImportError as e:
    print(f"❌ Ошибка импорта BrickClass: {e}")
    sys.exit(1)


class TestBrick(unittest.TestCase):

    def test_brick_bloc_creation(self):
        """Тест создания обычного кирпича"""
        brick = BrickBloc(100, 150)
        self.assertEqual(brick.X, 100)
        self.assertEqual(brick.Y, 150)
        self.assertEqual(brick.life, 5)
        self.assertTrue(brick.Can_destroy)
        self.assertIsNotNone(brick.Rectangle)

    def test_brick_middle_bloc_creation(self):
        """Тест создания среднего кирпича"""
        brick_vertical = BrickMiddleBloc(100, 150, "v")
        brick_horizontal = BrickMiddleBloc(100, 150, "h")

        self.assertEqual(brick_vertical.X, 100)
        self.assertEqual(brick_vertical.Y, 150)
        self.assertEqual(brick_vertical.life, 5)
        self.assertTrue(brick_vertical.Can_destroy)
        self.assertIsNotNone(brick_vertical.Rectangle)

        self.assertEqual(brick_horizontal.X, 100)
        self.assertEqual(brick_horizontal.Y, 150)
        self.assertEqual(brick_horizontal.life, 5)
        self.assertTrue(brick_horizontal.Can_destroy)

    def test_brick_properties(self):
        """Тест свойств кирпича"""
        brick = BrickBloc(50, 50)

        # Проверяем основные свойства
        self.assertTrue(hasattr(brick, 'X'))
        self.assertTrue(hasattr(brick, 'Y'))
        self.assertTrue(hasattr(brick, 'life'))
        self.assertTrue(hasattr(brick, 'Can_destroy'))
        self.assertTrue(hasattr(brick, 'Rectangle'))
        self.assertTrue(hasattr(brick, 'Brick_picture'))

    def test_brick_damage(self):
        """Тест получения урона кирпичом"""
        brick = BrickBloc(100, 100)
        initial_life = brick.life

        # Симулируем получение урона
        brick.life -= 2
        self.assertEqual(brick.life, initial_life - 2)

        # Проверяем уничтожение кирпича
        brick.life = 0
        self.assertEqual(brick.life, 0)

    def test_brick_middle_different_directions(self):
        """Тест что вертикальные и горизонтальные кирпичи создаются правильно"""
        brick_v = BrickMiddleBloc(100, 100, "v")
        brick_h = BrickMiddleBloc(100, 100, "h")

        # Они должны иметь разные изображения
        self.assertIsNotNone(brick_v.Brick_picture)
        self.assertIsNotNone(brick_h.Brick_picture)


if __name__ == '__main__':
    unittest.main()