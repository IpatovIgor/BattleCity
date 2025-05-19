import pygame
import MenuClass


pygame.init()
screen = pygame.display.set_mode((800, 512))
menu = MenuClass.Menu(screen)
menu.start()
