# test_game_logic.py
import unittest
import sys
import os

# Добавляем путь к модулям игры
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from BulletClass import Bullet
from BaseClass import Base
from BrickClass import BrickBloc


class TestGameLogic(unittest.TestCase):

    def test_bullet_initialization(self):
        """Тест инициализации пули"""
        bullet = Bullet("Up", 100, 100, 2)
        self.assertEqual(bullet.Direction, "Up")
        self.assertEqual(bullet.X, 100)
        self.assertEqual(bullet.Y, 100)
        self.assertEqual(bullet.Damage, 2)
        self.assertFalse(bullet.Is_boom)


    def test_brick_creation(self):
        """Тест создания кирпичных блоков"""
        brick = BrickBloc(50, 50)
        self.assertEqual(brick.X, 50)
        self.assertEqual(brick.Y, 50)
        self.assertEqual(brick.life, 5)
        self.assertTrue(brick.Can_destroy)


if __name__ == '__main__':
    unittest.main()
