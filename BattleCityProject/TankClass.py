import pygame
import BulletClass
import random
import threading


class Tank:
    Direction = 0
    Go_forward = 0
    Wait = 0
    Need_to_shoot = 0
    tank_status = 0
    Spawn_animation = [pygame.transform.scale(pygame.image.load('Images/Spawn1.png'), (43, 43)),
                       pygame.transform.scale(pygame.image.load('Images/Spawn2.png'), (43, 43)),
                       pygame.transform.scale(pygame.image.load('Images/Spawn3.png'), (43, 43)),
                       pygame.transform.scale(pygame.image.load('Images/Spawn4.png'), (43, 43))]
    Animation_list = 0
    Boom_animation = [pygame.transform.scale(pygame.image.load('Images/TankBoom1.png'), (34, 34)),
                      pygame.transform.scale(pygame.image.load('Images/TankBoom1.png'), (43, 43))]
    Spawn_slide = 0
    Speed = 4
    Can_destroy = True
    life = 10
    X = -1
    Y = -1
    Is_spawn = True
    Rectangle = -1
    Boom_animation_slide = 0
    IsBoom = False
    WasBoom = False
    next_dir = -1
    Timer = 0
    Damage = 0

    def __init__(self, tank_x, tank_y, animation, speed, damage):
        self.X = tank_x
        self.Y = tank_y
        self.Rectangle = self.Spawn_animation[self.Spawn_slide].get_rect(topleft=(tank_x, tank_y))
        timer = threading.Timer(4.0, self.stop_spawn_animation)
        timer.start()
        self.Animation_list = animation
        self.Speed = speed
        self.Damage = damage

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def stop_spawn_animation(self):
        self.Is_spawn = False

    def print(self, surface):
        surface.blit(self.Animation_list[self.Direction][self.tank_status], (self.X, self.Y))

    def print_boom(self, surface):
        surface.blit(self.Boom_animation[self.Boom_animation_slide], (self.X, self.Y))

    def print_spawn(self, surface):
        surface.blit(self.Spawn_animation[self.Spawn_slide], (self.X, self.Y))
        self.Spawn_slide += 1
        self.Spawn_slide %= 4

    def can_move(self, x, y, brick_list):
        if 0 > x or x > 620:
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
            bullet = BulletClass.Bullet("Up", self.X + 14, self.Y - 5, self.Damage)
        elif self.Direction == 1:
            bullet = BulletClass.Bullet("Right", self.X + 38, self.Y + 14, self.Damage)
        elif self.Direction == 2:
            bullet = BulletClass.Bullet("Down", self.X + 14, self.Y + 38, self.Damage)
        elif self.Direction == 3:
            bullet = BulletClass.Bullet("Left", self.X - 2, self.Y + 14, self.Damage)
        bullet_list.append(bullet)

    def update(self, object_list, screen, bullet_list):
        if self.Is_spawn:
            self.print_spawn(screen)
            return
        if self.life <= 0:
            self.IsBoom = True
        if self.Boom_animation_slide == 2:
            self.WasBoom = True
            return
        if self.IsBoom:
            self.print_boom(screen)
            self.Boom_animation_slide += 1
            return
        if self.Go_forward <= 0:
            self.next_dir = random.randint(0, 3)
            self.Go_forward = random.randint(20, 200)
            self.Wait = random.randint(0, 3)

        self.Need_to_shoot = random.randint(0, 15)
        if self.Wait != 3:
            if self.next_dir == 0:
                self.move_up(object_list)
            if self.next_dir == 1:
                self.move_right(object_list)
            if self.next_dir == 2:
                self.move_down(object_list)
            if self.next_dir == 3:
                self.move_left(object_list)
        if self.Need_to_shoot == 10:
            self.shoot(bullet_list)
        self.Go_forward -= self.Speed
        self.print(screen)
