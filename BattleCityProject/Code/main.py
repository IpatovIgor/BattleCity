import pygame
import MenuClass


pygame.init()
icon = pygame.image.load('../Images/Icon.jpg')
pygame.display.set_caption("IgorOfTank")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 512))
menu = MenuClass.Menu(screen)
menu.start()
