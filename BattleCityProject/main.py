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
import MenuClass


pygame.init()
screen = pygame.display.set_mode((800, 512))
menu = MenuClass.Menu(screen)
menu.Start()