import pygame
import BrickClass
import IronClass
import WaterClass
import BaseClass
import BrushClass
import LevelClass


class Menu:
    def __init__(self, screen):
        self.Screen = screen

    Bullet_list = []
    Brush = []
    Tank_limit = 0
    Objects_in_map = []
    Level_music = 0

    def create_first_level(self):
        self.Level_music = 'Music/Music_level1.mp3'
        self.Tank_limit = 7
        self.Brush = []
        self.Bullet_list = []
        self.Objects_in_map = [BrickClass.Brick_midle_bloc(310, 480, "v"), BrickClass.Brick_midle_bloc(310, 448, "v"),
                               BrickClass.Brick_midle_bloc(310, 432, "h"), BrickClass.Brick_midle_bloc(342, 432, "h"),
                               BrickClass.Brick_midle_bloc(374, 432, "h"), BrickClass.Brick_midle_bloc(390, 448, "v"),
                               BrickClass.Brick_midle_bloc(390, 480, "v"), BaseClass.Base(330, 460)]
        for i in range(4):
            for j in range(7):
                self.Objects_in_map.append(BrickClass.Brick_bloc(140 * (1 + i), j * 32))

        for i in range(8):
            self.Objects_in_map.append(IronClass.IronBlock(i * 90, 350))

        for i in range(9):
            self.Brush.append(BrushClass.Brush(i * 32, 480))
        for i in range(8):
            self.Brush.append(BrushClass.Brush(640 - i * 32, 480))

    def create_second_level(self):
        self.Level_music = 'Music/Music_level2.mp3'
        self.Tank_limit = 7
        self.Brush = []
        self.Bullet_list = []
        self.Objects_in_map = [BrickClass.Brick_midle_bloc(310, 480, "v"), BrickClass.Brick_midle_bloc(310, 448, "v"),
                               BrickClass.Brick_midle_bloc(310, 432, "h"), BrickClass.Brick_midle_bloc(342, 432, "h"),
                               BrickClass.Brick_midle_bloc(374, 432, "h"), BrickClass.Brick_midle_bloc(390, 448, "v"),
                               BrickClass.Brick_midle_bloc(390, 480, "v"), BaseClass.Base(330, 460)]
        for i in range(5):
            self.Brush.append(BrushClass.Brush(32 * i, 160))
            self.Brush.append(BrushClass.Brush(500 + 32 * i, 160))
            self.Brush.append(BrushClass.Brush(250 + 32 * i, 160))
            for j in range(5):
                self.Objects_in_map.append(WaterClass.Water_bloc(32 * i, 32 * j))
                self.Objects_in_map.append(WaterClass.Water_bloc(500 + 32 * i, 32 * j))
                self.Objects_in_map.append(WaterClass.Water_bloc(250 + 32 * i, 32 * j))
                self.Brush.append(BrushClass.Brush(20 + 32 * i, 250 + 32 * j))
                self.Brush.append(BrushClass.Brush(490 + 32 * i, 250 + 32 * j))

        for i in range(7):
            self.Objects_in_map.append(BrickClass.Brick_midle_bloc(332, 192 + i + 32 * i, "v"))
            self.Objects_in_map.append(IronClass.IronBlock(300, 192 + i + 32 * i))
            self.Objects_in_map.append(IronClass.IronBlock(346, 192 + i + 32 * i))

    def create_third_level(self):
        self.Level_music = 'Music/Music_level3.mp3'
        self.Tank_limit = 7
        self.Brush = []
        self.Bullet_list = []
        self.Objects_in_map = [BrickClass.Brick_midle_bloc(310, 480, "v"), BrickClass.Brick_midle_bloc(310, 448, "v"),
                               BrickClass.Brick_midle_bloc(310, 432, "h"), BrickClass.Brick_midle_bloc(342, 432, "h"),
                               BrickClass.Brick_midle_bloc(374, 432, "h"), BrickClass.Brick_midle_bloc(390, 448, "v"),
                               BrickClass.Brick_midle_bloc(390, 480, "v"), BaseClass.Base(330, 460)]
        for i in range(21):
            for j in range(10):
                if 7 <= i <= 15 and 4 <= j <= 6:
                    self.Objects_in_map.append(WaterClass.Water_bloc(4 + i * 32, j * 32))
                    continue
                self.Brush.append(BrushClass.Brush(4 + i * 32, j * 32))
        for i in range(14, 21):
            for j in range(10, 15):
                self.Brush.append(BrushClass.Brush(4 + i * 32, j * 32))
                self.Brush.append(BrushClass.Brush(4 + (i - 14) * 32, j * 32))
        for i in range(5):
            self.Objects_in_map.append(BrickClass.Brick_bloc(280 + i * 32, 400))

    Screen = 0
    Level_was_won = True
    Back_ground = pygame.transform.scale(pygame.image.load('Images/backGround.png'), (800, 512))
    Level_num = 1
    Game_was_won = False

    def start(self):
        pygame.mixer.music.load('Music/MenuMusic.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        win_ground = pygame.transform.scale(pygame.image.load('Images/YouWin.jpg'), (800, 512))
        back_ground_image = pygame.transform.scale(pygame.image.load('Images/Menu.jpg'), (800, 512))
        start_level_button = pygame.font.Font('Fonts/Merriweather-Italic-VariableFont_opsz,wdth,wght.ttf', 50)
        start_level_button = start_level_button.render("Strat level", False, (0, 0, 0))
        start_level_back = pygame.transform.scale(pygame.image.load('Images/White.png'), (225, 50))
        start_level_rect = start_level_button.get_rect(topleft=(300, 200))

        exit_button = pygame.font.Font('Fonts/Merriweather-Italic-VariableFont_opsz,wdth,wght.ttf', 40)
        exit_back = pygame.transform.scale(pygame.image.load('Images/White.png'), (70, 50))
        exit_button = exit_button.render("Exit", False, (0, 0, 0))
        exit_rect = exit_button.get_rect(topleft=(350, 270))
        clock = pygame.time.Clock()
        running = True
        while running:
            self.Screen.blit(back_ground_image, (0, 0))
            if self.Level_num == 4 or self.Level_was_won is False:
                if self.Level_num == 4 and self.Level_was_won:
                    self.Game_was_won = True
                self.Level_num = 1
            if self.Game_was_won:
                self.Screen.blit(win_ground, (0, 0))
            self.Screen.blit(exit_back, (350, 270))
            self.Screen.blit(exit_button, (350, 270))
            self.Screen.blit(start_level_back, (270, 185))
            self.Screen.blit(start_level_button, (270, 180))
            mouse = pygame.mouse.get_pos()
            if exit_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                quit()
            elif start_level_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.Game_was_won = False
                if self.Level_num == 1:
                    self.create_first_level()
                elif self.Level_num == 2:
                    self.create_second_level()
                else:
                    self.create_third_level()
                level = LevelClass.Level(self.Bullet_list, self.Brush, self.Objects_in_map, self.Screen,
                                         self.Level_num, self.Tank_limit)
                pygame.mixer.music.stop()
                self.Level_was_won = level.Start(self.Level_music)
                pygame.mixer.music.load('Music/MenuMusic.mp3')
                pygame.mixer.music.play(-1)
                self.Level_num += 1
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            clock.tick(15)
