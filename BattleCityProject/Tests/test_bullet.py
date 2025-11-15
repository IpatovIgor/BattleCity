# test_bullet.py
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
    from BulletClass import Bullet

    print("✓ BulletClass успешно импортирован")
except ImportError as e:
    print(f"❌ Ошибка импорта BulletClass: {e}")
    sys.exit(1)


class TestBullet(unittest.TestCase):

    def test_bullet_creation(self):
        """Тест создания пули"""
        bullet = Bullet("Up", 100, 100, 2)
        self.assertEqual(bullet.Direction, "Up")
        self.assertEqual(bullet.X, 100)
        self.assertEqual(bullet.Y, 100)
        self.assertEqual(bullet.Damage, 2)
        self.assertFalse(bullet.Is_boom)

    def test_bullet_properties(self):
        """Тест свойств пули"""
        bullet = Bullet("Right", 50, 50, 1)

        # Проверяем существующие свойства
        self.assertTrue(hasattr(bullet, 'Speed'))
        self.assertTrue(hasattr(bullet, 'Damage'))
        self.assertTrue(hasattr(bullet, 'Direction'))
        self.assertTrue(hasattr(bullet, 'X'))
        self.assertTrue(hasattr(bullet, 'Y'))
        self.assertTrue(hasattr(bullet, 'Is_boom'))
        self.assertTrue(hasattr(bullet, 'Was_boom'))
        self.assertTrue(hasattr(bullet, 'Animation_dir'))
        self.assertTrue(hasattr(bullet, 'Boom_animation_slide'))

    def test_bullet_movement(self):
        """Тест движения пули"""
        bullet = Bullet("Down", 200, 200, 2)
        initial_y = bullet.Y

        # Тестируем движение вниз
        bullet.move_down([])
        self.assertEqual(bullet.Y, initial_y + bullet.Speed)

        # Тестируем движение вверх
        bullet_up = Bullet("Up", 200, 200, 2)
        initial_y_up = bullet_up.Y
        bullet_up.move_up([])
        self.assertEqual(bullet_up.Y, initial_y_up - bullet_up.Speed)

    def test_bullet_collision_detection(self):
        """Тест обнаружения столкновений"""
        bullet = Bullet("Right", 100, 100, 2)

        # Тестируем движение без препятствий
        can_move = bullet.can_move(110, 100, [])
        self.assertTrue(can_move)

        # Тестируем движение за границы экрана
        can_move_out = bullet.can_move(-10, 100, [])
        self.assertFalse(can_move_out)

    def test_bullet_direction_animation(self):
        """Тест связи направления и анимации"""
        bullet_up = Bullet("Up", 100, 100, 2)
        bullet_right = Bullet("Right", 100, 100, 2)
        bullet_down = Bullet("Down", 100, 100, 2)
        bullet_left = Bullet("Left", 100, 100, 2)

        # Проверяем, что анимация устанавливается правильно
        bullet_up.move_up([])
        self.assertEqual(bullet_up.Animation_dir, 0)

        bullet_right.move_right([])
        self.assertEqual(bullet_right.Animation_dir, 3)

        bullet_down.move_down([])
        self.assertEqual(bullet_down.Animation_dir, 2)

        bullet_left.move_left([])
        self.assertEqual(bullet_left.Animation_dir, 1)


if __name__ == '__main__':
    unittest.main()
