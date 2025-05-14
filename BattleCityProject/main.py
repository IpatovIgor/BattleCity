import pygame
import BrickClass
import PlayerClass
import BulletClass
import IronClass
import WaterClass
import TankClass
import UpdateClass
import BaseClass
import BrushClass
import LevelClass


pygame.init()
screen = pygame.display.set_mode((800, 512))
space_pressed_prev = False

bullet_list = []
brush = []
objects_in_map = [BrickClass.Brick_midle_bloc(310, 480, "v"), BrickClass.Brick_midle_bloc(310, 448, "v"),
                  BrickClass.Brick_midle_bloc(310, 432, "h"), BrickClass.Brick_midle_bloc(342, 432, "h"),
                  BrickClass.Brick_midle_bloc(374, 432, "h"), BrickClass.Brick_midle_bloc(390, 448, "v"),
                  BrickClass.Brick_midle_bloc(390, 480, "v"),
                  BaseClass.Base(330, 460)]
for i in range(4):
    for j in range(7):
        objects_in_map.append(BrickClass.Brick_bloc(140 * (1 + i), j * 32))

for i in range(8):
    objects_in_map.append(IronClass.IronBlock(i * 80, 350))

for i in range(9):
    brush.append(BrushClass.Brush(i * 32, 480))
for i in range(8):
    brush.append(BrushClass.Brush(640 - i * 32, 480))

level1 = LevelClass.Level(bullet_list, brush, objects_in_map, screen)
level1.Start()