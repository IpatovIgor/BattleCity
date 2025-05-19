import pygame
import PlayerClass
import TankClass
import random


class PlayerSpawn:
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
    Normal_tank = [[pygame.transform.scale(pygame.image.load('Images/GreenTank11.png'), (34, 43)),
                    pygame.transform.scale(pygame.image.load('Images/GreenTank12.png'), (34, 43))],
                   [pygame.transform.scale(pygame.image.load('Images/GreenTank21.png'), (43, 34)),
                    pygame.transform.scale(pygame.image.load('Images/GreenTank22.png'), (43, 34))],
                   [pygame.transform.scale(pygame.image.load('Images/GreenTank31.png'), (34, 43)),
                    pygame.transform.scale(pygame.image.load('Images/GreenTank32.png'), (34, 43))],
                   [pygame.transform.scale(pygame.image.load('Images/GreenTank41.png'), (43, 34)),
                    pygame.transform.scale(pygame.image.load('Images/GreenTank42.png'), (43, 34))]]

    Fast_tank = [[pygame.transform.scale(pygame.image.load('Images/FastTank11.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/fastTank12.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/FastTank21.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/FastTank22.png'), (43, 34))],
                 [pygame.transform.scale(pygame.image.load('Images/FastTank31.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/FastTank32.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/FastTank41.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/FastTank42.png'), (43, 34))]]

    def Can_spawn(self, x, y):
        rect = pygame.transform.scale(pygame.image.load('Images/GreenTank11.png'), (34, 43)).get_rect(topleft=(x, y))
        for obj in self.Object_list:
            if rect.colliderect(obj.Rectangle):
                return False
        return True

    def Spawn(self):
        self.X = random.randint(1, 640)
        self.Y = random.randint(1, 120)
        type_of_tank = random.randint(1, 2)
        if self.Count_of_tanks < 4 and self.Can_spawn(self.X, self.Y) and self.Tank_was_spawn < self.Tank_limit:
            if type_of_tank == 1:
                self.Object_list.append(TankClass.Tank(self.X, self.Y, self.Normal_tank, 4, 2))
            elif type_of_tank == 2:
                self.Object_list.append(TankClass.Tank(self.X, self.Y, self.Fast_tank, 7, 1))
            self.Tank_was_spawn += 1
            self.Count_of_tanks += 1
