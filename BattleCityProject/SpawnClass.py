import pygame
import PlayerClass
import TankClass
import random


class Player_spawn:
    def __init__(self, x, y, object_list):
        self.X = x
        self.Y = y
        self.Object_list = object_list

    Object_list = []
    X = 0
    Y = 0
    Count_of_Plyer = 0

    def Spawn(self):
        if self.Count_of_Plyer == 0:
            self.Object_list.append(PlayerClass.Player(self.X, self.Y))
            self.Count_of_Plyer = 1


class Tank_spawn:
    def __init__(self, object_list, tank_limit):
        self.Object_list = object_list
        self.Tank_limit = tank_limit

    Object_list = []
    Count_of_tanks = 0
    X = 0
    Y = 0
    Tank_was_spawn = 0
    Tank_limit = 10

    def Can_spawn(self, x, y):
        rect = pygame.transform.scale(pygame.image.load('Images/GreenTank11.png'), (34, 43)).get_rect(topleft=(x, y))
        for obj in self.Object_list:
            if rect.colliderect(obj.Rectangle):
                return False
        return True


    def Spawn(self):
        self.X = random.randint(1, 640)
        self.Y = random.randint(1, 400)
        if self.Count_of_tanks < 4 and self.Can_spawn(self.X, self.Y) and self.Tank_was_spawn < self.Tank_limit:
            self.Object_list.append(TankClass.Tank(self.X, self.Y))
            self.Tank_was_spawn += 1
            self.Count_of_tanks += 1