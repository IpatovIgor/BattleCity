# test_integration.py
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PlayerClass import Player
from BulletClass import Bullet


class TestIntegration(unittest.TestCase):

    def test_player_shooting(self):
        """Тест системы стрельбы игрока"""
        player = Player(100, 100)
        bullet_list = []

        # Игрок стреляет
        player.shoot(bullet_list)

        # Проверяем, что пуля добавлена в список
        self.assertEqual(len(bullet_list), 1)

        bullet = bullet_list[0]
        self.assertIsInstance(bullet, Bullet)
        self.assertEqual(bullet.Damage, 2)

    def test_bullet_movement(self):
        """Тест движения пули"""
        bullet = Bullet("Up", 100, 100, 2)
        initial_y = bullet.Y

        # Двигаем пулю вверх
        bullet.move_up([])  # Пустой список объектов - нет столкновений

        self.assertEqual(bullet.Y, initial_y - bullet.Speed)


if __name__ == '__main__':
    unittest.main()