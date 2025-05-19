import pygame


class Base:
    def __init__(self, x, y):
        self.Rectangle = self.Base_picture[0].get_rect(topleft=(x, y))
        self.X = x
        self.Y = y

    Base_picture = [pygame.transform.scale(pygame.image.load('Images/Bird.png'), (50, 50)),
                    pygame.transform.scale(pygame.image.load('Images/Bull.png'), (50, 50))]
    Base_slide = 0
    Rectangle = -1
    Can_destroy = True
    life = 1
    X = 0
    Y = 0

    def print(self, surface):
        if self.life <= 0:
            self.Base_slide = 1

        surface.blit(self.Base_picture[self.Base_slide], (self.X, self.Y))
