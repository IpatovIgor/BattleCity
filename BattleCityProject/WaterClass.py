import pygame


class WaterBloc:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.Rectangle = self.Brick_picture.get_rect(topleft=(x, y))

    Brick_picture = pygame.transform.scale(pygame.image.load('Images/Water.png'), (32, 32))
    Rectangle = -1
    Can_destroy = False
    X = -1
    Y = -1

    life = 5

    def print(self, surface):
        surface.blit(self.Brick_picture, (self.X, self.Y))
