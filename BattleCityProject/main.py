import pygame
import BrickClass
import PlayerClass
import BulletClass
import IronClass
import WaterClass
import TankClass


pygame.init()
screen = pygame.display.set_mode((800, 512))
clock = pygame.time.Clock()

back_ground_image = pygame.image.load('Images/backGround.png')
back_ground_image = pygame.transform.scale(back_ground_image, (800, 512))
player = PlayerClass.Player(100, 100)
space_pressed_prev = False

bullet_list = []
objects_int_map = [BrickClass.Brick_bloc(200, 200), IronClass.IronBlock(400, 400), BrickClass.Brick_midle_bloc(50, 50, "v"),
                   WaterClass.Water_bloc(300, 50), TankClass.Tank(450, 50)]

running = True
while running:
    screen.blit(back_ground_image, (0, 0))
    player.Print(screen)

    was_removed = 0
    for i in range(len(objects_int_map)):
        if type(objects_int_map[i - was_removed]) == TankClass.Tank:
            if objects_int_map[i - was_removed].WasBoom:
                objects_int_map.pop(i - was_removed)
            else:
                objects_int_map[i - was_removed].Update(objects_int_map, screen, bullet_list)
        else:
            if objects_int_map[i - was_removed].life <= 0:
                objects_int_map.pop(i - was_removed)
                was_removed += 1
            else:
                objects_int_map[i - was_removed].Print(screen)

    was_boomed = 0
    for bullet_index in range(len(bullet_list)):
        if bullet_list[bullet_index - was_boomed].Was_boom is True:
            bullet_list.pop(bullet_index - was_boomed)
            was_boomed += 1
        else:
            bullet_list[bullet_index - was_boomed].Update(screen, objects_int_map)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.Move_up(objects_int_map)
    elif keys[pygame.K_s]:
        player.Move_down(objects_int_map)
    elif keys[pygame.K_d]:
        player.Move_right(objects_int_map)
    elif keys[pygame.K_a]:
        player.Move_left(objects_int_map)
    if keys[pygame.K_SPACE] and space_pressed_prev is False:
        player.Shoot(bullet_list)
        space_pressed_prev = True
    if keys[pygame.K_SPACE] is False:
        space_pressed_prev = False

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    clock.tick(15)