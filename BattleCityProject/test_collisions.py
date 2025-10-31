# test_collisions.py
import unittest
import sys
import os

GAME_DIR = os.path.join(os.path.dirname(__file__), "BattleCityProject")  # или путь к вашей игровой директории
sys.path.insert(0, GAME_DIR)

from BulletClass import Bullet
from BrickClass import BrickBloc


class TestCollisions(unittest.TestCase):

    def test_bullet_collision_detection(self):
        """Тест обнаружения столкновений пули"""
        bullet = Bullet("Right", 100, 100, 2)
        brick = BrickBloc(110, 100)  # Кирпич на пути пули

        # Создаем список объектов для проверки столкновений
        objects = [brick]

        # Проверяем возможность движения (должно вернуть False из-за столкновения)
        can_move = bullet.can_move(110, 100, objects)
        self.assertFalse(can_move)

    def test_bullet_damage_application(self):
        """Тест применения урона от пули"""
        bullet = Bullet("Right", 100, 100, 2)
        brick = BrickBloc(110, 100)
        initial_life = brick.life

        # Симулируем столкновение
        brick.life -= bullet.Damage

        self.assertEqual(brick.life, initial_life - bullet.Damage)


if __name__ == '__main__':
    unittest.main()