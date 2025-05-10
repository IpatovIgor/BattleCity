import pygame
import BulletClass


class Player:
    Direction = 0
    tank_status = 0
    Animation_list = [[pygame.transform.scale(pygame.image.load('Images/TankYellow1.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow5.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/TankYellow2.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow6.png'), (43, 34))],
                 [pygame.transform.scale(pygame.image.load('Images/TankYellow3.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow7.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/TankYellow4.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow8.png'), (43, 34))]]
    Speed = 4
    X = -1
    Y = -1
    rectangle = -1

    def __init__(self, tank_x, tank_y):
        self.X = tank_x
        self.Y = tank_y
        self.rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(tank_x, tank_y))

    def Print(self, surface):
        surface.blit(self.Animation_list[self.Direction][self.tank_status], (self.X, self.Y))

    def Can_move(self, x, y, brick_list):
        if 0 > x or x > 757:
            return False
        if 0 > y or y > 469:
            return False
        rect = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(x, y))
        for brick in brick_list:
            if rect.colliderect(brick.Rectangle):
                return False
        return True

    def Move_up(self, brick_list):
        self.Direction = 0
        can_move = self.Can_move(self.X, self.Y - self.Speed, brick_list)
        if can_move:
            self.Y -= self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def Move_down(self, brick_list):
        self.Direction = 2
        can_move = self.Can_move(self.X, self.Y + self.Speed, brick_list)
        if can_move:
            self.Y += self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def Move_left(self, brick_list):
        self.Direction = 3
        can_move = self.Can_move(self.X - self.Speed, self.Y, brick_list)
        if can_move:
            self.X -= self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def Move_right(self, brick_list):
        self.Direction = 1
        can_move = self.Can_move(self.X + self.Speed + 1, self.Y, brick_list)
        if can_move:
            self.X += self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def Shoot(self, bullet_list):
        bullet = -1
        if self.Direction == 0:
            bullet = BulletClass.Bullet("Up", self.X + 14, self.Y - 5)
        elif self.Direction == 1:
            bullet = BulletClass.Bullet("Right", self.X + 38, self.Y + 14)
        elif self.Direction == 2:
            bullet = BulletClass.Bullet("Down", self.X + 14, self.Y + 38)
        elif self.Direction == 3:
            bullet = BulletClass.Bullet("Left", self.X - 2, self.Y + 14)
        bullet_list.append(bullet)