import pygame
import BrickClass
import PlayerClass
import BulletClass
import IronClass
import WaterClass
import TankClass
import UpdateClass
import BaseClass


pygame.init()
screen = pygame.display.set_mode((800, 512))
clock = pygame.time.Clock()

back_ground_image = pygame.image.load('Images/backGround.png')
back_ground_image = pygame.transform.scale(back_ground_image, (800, 512))
space_pressed_prev = False

bullet_list = []
objects_int_map = [BrickClass.Brick_bloc(200, 200), IronClass.IronBlock(400, 400), BrickClass.Brick_midle_bloc(50, 50, "v"),
                   WaterClass.Water_bloc(300, 50), BaseClass.Base(400, 100)]
updater = UpdateClass.Update(bullet_list, objects_int_map, screen)

running = True
while running:
    screen.blit(back_ground_image, (0, 0))

    updater.Update_object()
    updater.Update_bullets()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if updater.Game_is_Lost:
        pygame.quit()
        running = False

    clock.tick(15)