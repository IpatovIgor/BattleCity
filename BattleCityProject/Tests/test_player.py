# test_player.py
import unittest
import sys
import os

# Импортируем конфигурацию первым делом
from test_config import PATHS_SETUP
from test_utils import setup_test_environment, create_mock_surface

if not PATHS_SETUP:
    print("❌ Не удалось настроить пути! Тесты не могут быть запущены.")
    sys.exit(1)

# Настраиваем тестовое окружение
setup_test_environment()

try:
    from PlayerClass import Player
    from BulletClass import Bullet

    print("✓ PlayerClass и BulletClass успешно импортированы")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом"""
        self.mock_screen = create_mock_surface()
        self.player = Player(100, 100)
        self.player.Screen = self.mock_screen

    def test_player_creation(self):
        """Тест создания игрока"""
        self.assertEqual(self.player.X, 100)
        self.assertEqual(self.player.Y, 100)
        self.assertEqual(self.player.life, 2)
        self.assertEqual(self.player.Speed, 4)
        self.assertEqual(self.player.Direction, 0)
        self.assertFalse(self.player.Can_to_die)
        self.assertIsNotNone(self.player.Rectangle)

    def test_player_shooting(self):
        """Тест стрельбы игрока"""
        bullet_list = []

        # Игрок стреляет
        self.player.shoot(bullet_list)

        # Проверяем, что пуля добавлена
        self.assertEqual(len(bullet_list), 1)
        bullet = bullet_list[0]

        # Проверяем что это объект Bullet (используем тип для сравнения)
        self.assertEqual(type(bullet).__name__, 'Bullet')

        # Проверяем свойства пули
        self.assertEqual(bullet.Damage, 2)

    def test_player_movement(self):
        """Тест движения игрока"""
        initial_x = self.player.X

        # Тестируем движение вправо
        self.player.move_right([])
        self.assertEqual(self.player.X, initial_x + self.player.Speed)
        self.assertEqual(self.player.Direction, 1)

    def test_player_properties(self):
        """Тест свойств игрока"""
        self.assertTrue(hasattr(self.player, 'life'))
        self.assertTrue(hasattr(self.player, 'Speed'))
        self.assertTrue(hasattr(self.player, 'Direction'))
        self.assertTrue(hasattr(self.player, 'X'))
        self.assertTrue(hasattr(self.player, 'Y'))
        self.assertTrue(hasattr(self.player, 'Rectangle'))
        self.assertTrue(hasattr(self.player, 'Can_to_die'))
        self.assertTrue(hasattr(self.player, 'IsBoom'))
        self.assertTrue(hasattr(self.player, 'WasBoom'))

    def test_player_collision_detection(self):
        """Тест обнаружения столкновений игрока"""
        # Тестируем движение без препятствий
        can_move = self.player.can_move(110, 100, [])
        self.assertTrue(can_move)

        # Тестируем движение за границы
        can_move_out = self.player.can_move(-10, 100, [])
        self.assertFalse(can_move_out)

    def test_player_direction_changes(self):
        """Тест изменения направления игрока"""
        # Двигаемся вверх
        self.player.move_up([])
        self.assertEqual(self.player.Direction, 0)

        # Двигаемся вправо
        self.player.move_right([])
        self.assertEqual(self.player.Direction, 1)

        # Двигаемся вниз
        self.player.move_down([])
        self.assertEqual(self.player.Direction, 2)

        # Двигаемся влево
        self.player.move_left([])
        self.assertEqual(self.player.Direction, 3)


if __name__ == '__main__':
    unittest.main()