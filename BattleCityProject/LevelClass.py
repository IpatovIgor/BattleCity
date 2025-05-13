import pygame
import BrickClass
import PlayerClass
import BulletClass
import IronClass
import WaterClass
import TankClass
import UpdateClass
import BaseClass
import BrushClass


class Level:
    def __init__(self, bullet_list, brush, objects_in_map, screen):
        self.Bullet_list = bullet_list
        self.Brush = brush
        self.Objects_in_map = objects_in_map
        self.Screen = screen

    Screen = 0
    Bullet_list = 0
    Brush = 0
    Objects_in_map = 0

    def Start(self):
        clock = pygame.time.Clock()
        stat_panel = pygame.Surface((120, 512))
        stat_panel.fill((255, 255, 255))
        back_ground_image = pygame.image.load('Images/backGround.png')
        back_ground_image = pygame.transform.scale(back_ground_image, (800, 512))
        panel_ground_image = pygame.image.load('Images/White.png')
        panel_ground_image = pygame.transform.scale(panel_ground_image, (120, 512))
        updater = UpdateClass.Update(self.Bullet_list, self.Objects_in_map, self.Screen, self.Brush, stat_panel)
        running = True
        while running:
            self.Screen.blit(back_ground_image, (0, 0))
            self.Screen.blit(stat_panel, (680, 0))
            stat_panel.blit(panel_ground_image, (0, 0))

            updater.Update_object()
            updater.Update_bullets()
            updater.Update_brush()
            updater.Update_stat()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            if updater.Game_is_Lost:
                pygame.quit()
                running = False

            clock.tick(15)