import pygame

import PlayerClass


class Bullet:
    Boom_animation_slide = 0
    Boom_animation = [[pygame.transform.scale(pygame.image.load('Images/Boom1.png'), (16, 16)), 5],
                      [pygame.transform.scale(pygame.image.load('Images/Boom2.png'), (18, 18)), 6],
                      [pygame.transform.scale(pygame.image.load('Images/Boom3.png'), (20, 20)), 7]]
    Drive_animation = [pygame.transform.scale(pygame.image.load('Images/Bullet1.png'), (6, 8)),
                       pygame.transform.scale(pygame.image.load('Images/Bullet2.png'), (8, 6)),
                       pygame.transform.scale(pygame.image.load('Images/Bullet3.png'), (6, 8)),
                       pygame.transform.scale(pygame.image.load('Images/Bullet4.png'), (8, 6))]
    X = -1
    Y = -1
    Speed = 10
    Damage = 2
    Direction = "Up"
    Animation_dir = 0
    Was_boom = False
    Is_boom = False

    def __init__(self, direction, x, y, damage):
        self.Direction = direction
        self.Damage = damage
        self.X = x
        self.Y = y

    def can_move(self, x, y, brick_list):
        if x < 0 or x > 660:
            self.Is_boom = True
            return False
        if y < 0 or y > 502:
            self.Is_boom = True
            return False
        rect = self.Drive_animation[self.Animation_dir].get_rect(topleft=(x, y))
        for brick in brick_list:
            if rect.colliderect(brick.Rectangle) and brick.Can_destroy is True:
                if type(brick) == PlayerClass.Player and brick.Can_to_die is False:
                    brick.life += self.Damage
                brick.life -= self.Damage
                self.Is_boom = True
                return False
        return True

    def move_up(self, brick_list):
        self.Animation_dir = 0
        can_move = self.can_move(self.X, self.Y - self.Speed, brick_list)
        if can_move:
            self.Y -= self.Speed
        else:
            self.Is_boom = True

    def move_down(self, brick_list):
        self.Animation_dir = 2
        can_move = self.can_move(self.X, self.Y + self.Speed, brick_list)
        if can_move:
            self.Y += self.Speed
        else:
            self.Is_boom = True

    def move_left(self, brick_list):
        self.Animation_dir = 1
        can_move = self.can_move(self.X - self.Speed, self.Y, brick_list)
        if can_move:
            self.X -= self.Speed
        else:
            self.Is_boom = True

    def move_right(self, brick_list):
        self.Animation_dir = 3
        can_move = self.can_move(self.X + self.Speed, self.Y, brick_list)
        if can_move:
            self.X = self.X + self.Speed
        else:
            self.Is_boom = True

    def print(self, surface):
        surface.blit(self.Drive_animation[self.Animation_dir], (self.X, self.Y))

    def print_boom(self, surface):
        x = self.X - self.Boom_animation[self.Boom_animation_slide][1]
        y = self.Y - self.Boom_animation[self.Boom_animation_slide][1]
        surface.blit(self.Boom_animation[self.Boom_animation_slide][0], (x, y))
        self.Boom_animation_slide += 1

    def update(self, screen, brick_list):
        if self.Boom_animation_slide == 3:
            self.Was_boom = True
            return
        if self.Is_boom is False:
            if self.Direction == "Up":
                self.move_up(brick_list)
            if self.Direction == "Left":
                self.move_left(brick_list)
            if self.Direction == "Right":
                self.move_right(brick_list)
            if self.Direction == "Down":
                self.move_down(brick_list)
            self.print(screen)
        else:
            self.print_boom(screen)
