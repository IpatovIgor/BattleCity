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
import threading


class Level:
    def __init__(self, bullet_list, brush, objects_in_map, screen, number_of_level, tank_limit):
        self.Tank_limit = tank_limit
        self.Bullet_list = bullet_list
        self.Number_of_level = number_of_level
        self.Brush = brush
        self.Objects_in_map = objects_in_map
        self.Screen = screen
        self.Timer = threading.Timer(3.0, self.Start_game)

    def Start_game(self):
        self.Game_is_started = True

    Timer = 0
    Tank_limit = 0
    Screen = 0
    Number_of_level = -1
    Game_is_started = False
    Bullet_list = 0
    Brush = 0
    Objects_in_map = 0
    Start_Images = [pygame.transform.scale(pygame.image.load('Images/Stage.png'), (400, 100)),
                    pygame.transform.scale(pygame.image.load('Images/Num1.png'), (100, 100)),
                    pygame.transform.scale(pygame.image.load('Images/Num2.png'), (100, 100)),
                    pygame.transform.scale(pygame.image.load('Images/Num3.png'), (100, 100))]

    def Show_start_Image(self):
        back_ground_image = pygame.transform.scale(pygame.image.load('Images/backGround.png'), (800, 512))
        self.Screen.blit(back_ground_image, (0, 0))
        self.Screen.blit(self.Start_Images[0], (150, 200))
        self.Screen.blit(self.Start_Images[self.Number_of_level], (550, 200))

    def Start(self):
        self.Timer.start()
        clock = pygame.time.Clock()
        stat_panel = pygame.Surface((120, 512))
        stat_panel.fill((255, 255, 255))
        back_ground_image = pygame.image.load('Images/backGround.png')
        back_ground_image = pygame.transform.scale(back_ground_image, (800, 512))
        panel_ground_image = pygame.image.load('Images/White.png')
        panel_ground_image = pygame.transform.scale(panel_ground_image, (120, 512))
        updater = UpdateClass.Update(self.Bullet_list, self.Objects_in_map, self.Screen, self.Brush, stat_panel, self.Tank_limit)
        running = True
        while running:
            if self.Game_is_started is False:
                self.Show_start_Image()
                pygame.display.update()
                continue
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
                    quit()

            if updater.Game_is_Lost:
                running = False

            clock.tick(15)

        return updater.Game_win