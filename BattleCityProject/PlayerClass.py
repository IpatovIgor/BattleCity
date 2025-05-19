import pygame
import BulletClass
import threading


class Player:
    Direction = 0
    Can_destroy = True
    life = 2
    tank_status = 0
    Boom_animation = [pygame.transform.scale(pygame.image.load('Images/TankBoom1.png'), (34, 34)),
                      pygame.transform.scale(pygame.image.load('Images/TankBoom1.png'), (43, 43))]
    IsBoom = False
    Can_to_die = False
    Non_die_animation_slide = 0
    WasBoom = False
    Boom_animation_slide = 0

    Non_die_animation = [pygame.transform.scale(pygame.image.load('Images/NonKill1.png'), (50, 50)),
                         pygame.transform.scale(pygame.image.load('Images/NonKill2.png'), (50, 50))]

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
    Rectangle = 0

    def __init__(self, tank_x, tank_y):
        self.X = tank_x
        self.Y = tank_y
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(tank_x, tank_y))
        timer = threading.Timer(6.0, self.make_plyer_can_die)
        timer.start()

    def make_plyer_can_die(self):
        self.Can_to_die = True

    def print(self, surface):
        if self.life <= 0:
            self.IsBoom = True
            if self.Boom_animation_slide == 2:
                self.WasBoom = True
            else:
                self.print_boom(surface)
                self.Boom_animation_slide += 1
            return

        surface.blit(self.Animation_list[self.Direction][self.tank_status], (self.X, self.Y))
        if self.Can_to_die is False:
            surface.blit(self.Non_die_animation[self.Non_die_animation_slide], (self.X - 5, self.Y - 5))
            self.Non_die_animation_slide += 1
            self.Non_die_animation_slide %= 2

    def print_boom(self, surface):
        surface.blit(self.Boom_animation[self.Boom_animation_slide], (self.X, self.Y))

    def can_move(self, x, y, brick_list):
        if 0 > x or x > 620:
            return False
        if 0 > y or y > 469:
            return False
        rect = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(x, y))
        for brick in brick_list:
            if type(brick) != Player and rect.colliderect(brick.Rectangle):
                return False
        return True

    def move_up(self, brick_list):
        prev_dir = self.Direction
        self.Direction = 0
        can_move = self.can_move(self.X, self.Y - self.Speed - 10, brick_list)
        if can_move:
            self.Y -= self.Speed
            if prev_dir != 0:
                self.Y -= 10
        else:
            self.Direction = prev_dir
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def move_down(self, brick_list):
        prev_dir = self.Direction
        self.Direction = 2
        can_move = self.can_move(self.X, self.Y + self.Speed, brick_list)
        if can_move:
            self.Y += self.Speed
        else:
            self.Direction = prev_dir
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def move_left(self, brick_list):
        prev_dir = self.Direction
        self.Direction = 3
        can_move = self.can_move(self.X - self.Speed - 10, self.Y, brick_list)
        if can_move:
            self.X -= self.Speed
            if prev_dir != 3:
                self.X -= 10
        else:
            self.Direction = prev_dir
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def move_right(self, brick_list):
        prev_dir = self.Direction
        self.Direction = 1
        can_move = self.can_move(self.X + self.Speed + 1, self.Y, brick_list)
        if can_move:
            self.X += self.Speed
        else:
            self.Direction = prev_dir
        self.tank_status += 1
        self.tank_status %= 2
        self.Rectangle = self.Animation_list[self.Direction][self.tank_status].get_rect(topleft=(self.X, self.Y))

    def shoot(self, bullet_list):
        bullet = -1
        if self.Direction == 0:
            bullet = BulletClass.Bullet("Up", self.X + 14, self.Y - 5, 2)
        elif self.Direction == 1:
            bullet = BulletClass.Bullet("Right", self.X + 38, self.Y + 14, 2)
        elif self.Direction == 2:
            bullet = BulletClass.Bullet("Down", self.X + 14, self.Y + 38, 2)
        elif self.Direction == 3:
            bullet = BulletClass.Bullet("Left", self.X - 2, self.Y + 14, 2)
        bullet_list.append(bullet)
