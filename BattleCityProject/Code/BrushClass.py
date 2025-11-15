import pygame


class Brush:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    Brick_picture = pygame.transform.scale(pygame.image.load('../Images/brush.png'), (32, 32))
    X = -1
    Y = -1

    life = 5

    def print(self, surface):
        surface.blit(self.Brick_picture, (self.X, self.Y))
