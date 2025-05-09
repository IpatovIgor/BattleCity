import pygame
import BulletClass
import random


class Tank:
    Direction = 0
    Go_forward = 0
    Wait = 0
    Need_to_shoot = 0
    tank_status = 0
    Animation_list = [[pygame.transform.scale(pygame.image.load('Images/GreenTank11.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/GreenTank12.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/GreenTank21.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/GreenTank22.png'), (43, 34))],
                 [pygame.transform.scale(pygame.image.load('Images/GreenTank31.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/GreenTank32.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/GreenTank41.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/GreenTank42.png'), (43, 34))]]
    Boom_animation = [pygame.transform.scale(pygame.image.load('Images/TankBoom1.png'), (34, 34)),
                      pygame.transform.scale(pygame.image.load('Images/TankBoom1.png'), (43, 43))]
    Speed = 4
    Can_destroy = True
    life = 10
    X = -1
    Y = -1
    Rectangle = -1
    Boom_animation_slide = 0
    IsBoom = False
    WasBoom = False

    def __init__(self, tank_x, tank_y):
        self.X = tank_x
        self.Y = tank_y
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(tank_x, tank_y))

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def Print(self, surface):
        surface.blit(self.Animation_list[self.Direction][self.tank_status], (self.X, self.Y))

    def Print_boom(self, surface):
        surface.blit(self.Boom_animation[self.Boom_animation_slide], (self.X, self.Y))

    def Can_move(self, x, y, brick_list):
        if 0 > x or x > 757:
            return False
        if 0 > y or y > 469:
            return False
        rect = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(x, y))
        for obj in brick_list:
            if type(obj) == Tank and self == obj:
                continue
            if rect.colliderect(obj.Rectangle):
                return False
        return True

    def Move_up(self, brick_list):
        self.Direction = 0
        can_move = self.Can_move(self.X, self.Y - self.Speed, brick_list)
        if can_move:
            self.Y -= self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def Move_down(self, brick_list):
        self.Direction = 2
        can_move = self.Can_move(self.X, self.Y + self.Speed, brick_list)
        if can_move:
            self.Y += self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def Move_left(self, brick_list):
        self.Direction = 3
        can_move = self.Can_move(self.X - self.Speed, self.Y, brick_list)
        if can_move:
            self.X -= self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def Move_right(self, brick_list):
        self.Direction = 1
        can_move = self.Can_move(self.X + self.Speed + 1, self.Y, brick_list)
        if can_move:
            self.X += self.Speed
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

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

    def Update(self, object_list, screen, bullet_list):
        if self.life <= 0:
            self.IsBoom = True
        if self.Boom_animation_slide == 2:
            self.WasBoom = True
            return
        if self.IsBoom:
            self.Print_boom(screen)
            self.Boom_animation_slide += 1
            return
        if self.Go_forward <= 0:
            self.Direction = random.randint(0, 3)
            self.Go_forward = random.randint(20, 100)
            self.Need_to_shoot = random.randint(0, 1)
            self.Wait = random.randint(0, 1)
            if self.Need_to_shoot:
                self.Shoot(bullet_list)

        if not self.Wait:
            if self.Direction == 0:
                self.Move_up(object_list)
            if self.Direction == 1:
                self.Move_right(object_list)
            if self.Direction == 2:
                self.Move_down(object_list)
            if self.Direction == 3:
                self.Move_left(object_list)

        self.Go_forward -= self.Speed
        self.Print(screen)