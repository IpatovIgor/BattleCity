import pygame
import threading
import BaseClass
import PlayerClass
import TankClass
import SpawnClass


class Update:
    def __init__(self, bullet_list, object_in_map, screen, brush_list, stat_panel, tank_limit):
        pygame.mixer.init()
        self.Bullet_list = bullet_list
        self.Objects_in_map = object_in_map
        self.Screen = screen
        self.timer = threading.Timer(3.0, self.Lost_game)
        self.Player_swan = SpawnClass.PlayerSpawn(150, 450, object_in_map)
        self.Tank_spawn = SpawnClass.Tank_spawn(object_in_map, tank_limit)
        self.Brush_list = brush_list
        self.Stat_panel = stat_panel
        self.Channel0 = pygame.mixer.Channel(0)
        self.Ride_sound = pygame.mixer.Sound("Music/RideSound.mp3")
        self.Channel1 = pygame.mixer.Channel(1)
        self.Shoot_sound = pygame.mixer.Sound("Music/Shoot.mp3")

    Game_over_image = [pygame.transform.scale(pygame.image.load('Images/GameOver.png'), (400, 200)),
                       pygame.transform.scale(pygame.image.load('Images/Pause.png'), (400, 150))]

    def Lost_game(self):
        self.Game_is_Lost = True

    Stat_panel = 0
    Tank_lifes = 3
    Spawn = 0
    timer = 0
    Timer_is_work = False
    Screen = 0
    Game_is_Lost = False
    Bullet_list = 0
    Objects_in_map = []
    Space_pressed_prev = False
    Player_swan = 0
    Tank_spawn = 0
    Brush_list = []
    Game_win = False
    Showing_game_over = False
    Back_ground_image = pygame.transform.scale(pygame.image.load('Images/backGround.png'), (800, 512))

    def Update_bullets(self):
        if self.Showing_game_over:
            self.Screen.blit(self.Back_ground_image, (0, 0))
            self.Screen.blit(self.Game_over_image[int(self.Game_win)], (200, 120))
            return
        was_boomed = 0
        for bullet_index in range(len(self.Bullet_list)):
            if self.Bullet_list[bullet_index - was_boomed].Was_boom is True:
                self.Bullet_list.pop(bullet_index - was_boomed)
                was_boomed += 1
            else:
                self.Bullet_list[bullet_index - was_boomed].Update(self.Screen, self.Objects_in_map)

    def Update_object(self):
        if self.Showing_game_over:
            return
        if self.Tank_lifes != 0:
            self.Player_swan.Spawn()
        was_removed = 0
        for i in range(len(self.Objects_in_map)):
            if type(self.Objects_in_map[i - was_removed]) == PlayerClass.Player:
                if self.Objects_in_map[i - was_removed].WasBoom:
                    self.Objects_in_map.pop(i - was_removed)
                    self.Tank_lifes -= 1
                    self.Player_swan.Count_of_Plyer = 0
                    was_removed += 1
                    if self.Tank_lifes == 0 and self.Timer_is_work is False:
                        self.timer.start()
                        self.Timer_is_work = True
                        self.Showing_game_over = True
                        return
                else:
                    self.Update_player(self.Objects_in_map[i - was_removed])
            elif type(self.Objects_in_map[i - was_removed]) == TankClass.Tank:
                if self.Objects_in_map[i - was_removed].WasBoom:
                    self.Objects_in_map.pop(i - was_removed)
                    self.Tank_spawn.Count_of_tanks -= 1
                    was_removed += 1
                else:
                    self.Objects_in_map[i - was_removed].Update(self.Objects_in_map, self.Screen, self.Bullet_list)
            elif type(self.Objects_in_map[i - was_removed]) == BaseClass.Base:
                if self.Objects_in_map[i - was_removed].life <= 0 and self.Timer_is_work is False:
                    self.timer.start()
                    self.Timer_is_work = True
                    self.Showing_game_over = True
                else:
                    self.Objects_in_map[i - was_removed].Print(self.Screen)
            else:
                if self.Objects_in_map[i - was_removed].life <= 0:
                    self.Objects_in_map.pop(i - was_removed)
                    was_removed += 1
                else:
                    self.Objects_in_map[i - was_removed].Print(self.Screen)
        self.Tank_spawn.Spawn()

        if self.Tank_spawn.Tank_was_spawn == self.Tank_spawn.Tank_limit and self.Tank_spawn.Count_of_tanks == 0 and self.Timer_is_work is False:
            self.timer.start()
            self.Showing_game_over = True
            self.Game_win = True
            self.Timer_is_work = True

    Channel0 = 0
    Ride_sound = 0
    Channel1 = 0
    Shoot_sound = 0

    def Update_player(self, player):
        if self.Showing_game_over:
            return
        player.Print(self.Screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.Move_up(self.Objects_in_map)
            if not self.Channel0.get_busy():
                self.Channel0.play(self.Ride_sound, loops=0)
        elif keys[pygame.K_s]:
            player.Move_down(self.Objects_in_map)
            if not self.Channel0.get_busy():
                self.Channel0.play(self.Ride_sound, loops=0)
        elif keys[pygame.K_d]:
            player.Move_right(self.Objects_in_map)
            if not self.Channel0.get_busy():
                self.Channel0.play(self.Ride_sound, loops=0)
        elif keys[pygame.K_a]:
            player.Move_left(self.Objects_in_map)
            if not self.Channel0.get_busy():
                self.Channel0.play(self.Ride_sound, loops=0)
        else:
            self.Channel0.stop()
        if keys[pygame.K_SPACE] and self.Space_pressed_prev is False:
            if self.Channel1.get_busy():
                self.Channel1.stop()
            self.Channel1.play(self.Shoot_sound, loops=0)
            player.Shoot(self.Bullet_list)
            self.Space_pressed_prev = True
        if keys[pygame.K_SPACE] is False:
            self.Space_pressed_prev = False

    def Update_brush(self):
        if self.Showing_game_over:
            return
        for brush in self.Brush_list:
            brush.Print(self.Screen)

    Heart = pygame.transform.scale(pygame.image.load('Images/Heart.png'), (30, 30))
    Tank_image = pygame.transform.scale(pygame.image.load('Images/GreenTank11.png'), (30, 30))

    def Update_stat(self):
        if self.Showing_game_over:
            return
        for i in range(self.Tank_lifes):
            self.Stat_panel.blit(self.Heart, (0 + i * 43, 0))

        for i in range(self.Tank_spawn.Tank_limit - self.Tank_spawn.Tank_was_spawn):
            self.Stat_panel.blit(self.Tank_image, (0 + (i % 2) * 43, (50 + (i // 2) * 50)))