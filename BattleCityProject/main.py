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
brush = [BrushClass.Brush(1, 400)]
objects_in_map = [BrickClass.Brick_midle_bloc(310, 480, "v"), BrickClass.Brick_midle_bloc(310, 448, "v"),
                  BrickClass.Brick_midle_bloc(310, 432, "h"), BrickClass.Brick_midle_bloc(342, 432, "h"),
                  BrickClass.Brick_midle_bloc(374, 432, "h"), BrickClass.Brick_midle_bloc(390, 448, "v"),
                  BrickClass.Brick_midle_bloc(390, 480, "v"),
                  BaseClass.Base(330, 460)]

level1 = LevelClass.Level(bullet_list, brush, objects_in_map, screen)
level1.Start()