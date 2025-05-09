import pygame

class Bullet:
    Boom_animation_slide = 0
    Boom_animation = [[pygame.transform.scale(pygame.image.load('Images/Boom1.png'), (16, 16)), 5],
                      [pygame.transform.scale(pygame.image.load('Images/Boom2.png'), (18, 18)), 6],
                      [pygame.transform.scale(pygame.image.load('Images/Boom3.png'), (20, 20)), 7],
                      [pygame.transform.scale(pygame.image.load('Images/Boom4.png'), (22, 22)), 8]]
    Drive_animation = [pygame.transform.scale(pygame.image.load('Images/Bullet1.png'), (6, 8)),
                 pygame.transform.scale(pygame.image.load('Images/Bullet2.png'), (8, 6)),
                 pygame.transform.scale(pygame.image.load('Images/Bullet3.png'), (6, 8)),
                 pygame.transform.scale(pygame.image.load('Images/Bullet4.png'), (8, 6))]
    X = -1
    Y = -1
    Speed = 10
    Direction = "Up"
    Animation_dir = 0
    Was_boom = False
    Is_boom = False

    def __init__(self, direction, x, y):
        self.Direction = direction
        self.X = x
        self.Y = y

    def Move_up(self):
        self.Animation_dir = 0
        if 0 >= self.Y - self.Speed:
            self.Y = 0
            self.Is_boom = True
        else:
            self.Y = self.Y - self.Speed

    def Move_down(self):
        self.Animation_dir = 2
        self.Y = min(512 - 20, self.Y + self.Speed)

    def Move_left(self):
        self.Animation_dir = 1
        self.X = max(0, self.X - self.Speed)

    def Move_right(self):
        self.Animation_dir = 3
        self.X = min(800 - 20, self.X + self.Speed)

    def Print(self, surface):
        surface.blit(self.Drive_animation[self.Animation_dir], (self.X, self.Y))

    def PrintBoom(self, surface):
        x = self.X - self.Boom_animation[self.Boom_animation_slide][1]
        y = self.Y - self.Boom_animation[self.Boom_animation_slide][1]
        surface.blit(self.Boom_animation[self.Boom_animation_slide][0], (x, y))
        self.Boom_animation_slide += 1

    def Update(self, screen):
        if self.Boom_animation_slide == 4:
            self.Was_boom = True
            return
        if self.Is_boom is False:
            if self.Direction == "Up":
                self.Move_up()
            if self.Direction == "Left":
                self.Move_left()
            if self.Direction == "Right":
                self.Move_right()
            if self.Direction == "Down":
                self.Move_down()
            self.Print(screen)
        else:
            self.PrintBoom(screen)




class Player:
    Direction = 0
    tank_status = 0
    Animation_list = [[pygame.transform.scale(pygame.image.load('Images/TankYellow1.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow5.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/TankYellow2.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow6.png'), (43, 34))],
                 [pygame.transform.scale(pygame.image.load('Images/TankYellow3.png'), (34, 43)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow7.png'), (34, 43))],
                 [pygame.transform.scale(pygame.image.load('Images/TankYellow4.png'), (43, 34)),
                  pygame.transform.scale(pygame.image.load('Images/TankYellow8.png'), (43, 34))]]
    Speed = 4
    X = -1
    Y = -1
    rectangle = Animation_list[Direction][tank_status].get_rect(topleft=(X, Y))

    def __init__(self, tank_x, tank_y):
        self.X = tank_x
        self.Y = tank_y
        self.tank_status += 1
        self.tank_status %= 2

    def Print(self, surface):
        surface.blit(self.Animation_list[self.Direction][self.tank_status], (self.X, self.Y))

    def Move_up(self):
        self.Direction = 0
        self.Y = max(0, self.Y - self.Speed)
        self.tank_status += 1
        self.tank_status %= 2

    def Move_down(self):
        self.Direction = 2
        self.Y = min(512 - 43, self.Y + self.Speed)
        self.tank_status += 1
        self.tank_status %= 2

    def Move_left(self):
        self.Direction = 3
        self.X = max(0, self.X - self.Speed)
        self.tank_status += 1
        self.tank_status %= 2

    def Move_right(self):
        self.Direction = 1
        self.X = min(800 - 43, self.X + self.Speed)
        self.tank_status += 1
        self.tank_status %= 2

    def Shoot(self, bullet_list):
        bullet = -1
        if self.Direction == 0:
            bullet = Bullet("Up", self.X + 14, self.Y - 5)
        elif self.Direction == 1:
            bullet = Bullet("Right", self.X + 38, self.Y + 14)
        elif self.Direction == 2:
            bullet = Bullet("Down", self.X + 14, self.Y + 38)
        elif self.Direction == 3:
            bullet = Bullet("Left", self.X - 2, self.Y + 14)
        bullet_list.append(bullet)


pygame.init()
screen = pygame.display.set_mode((800, 512))
clock = pygame.time.Clock()

back_ground_image = pygame.image.load('Images/backGround.png')
back_ground_image = pygame.transform.scale(back_ground_image, (800, 512))
tank_image = pygame.image.load('Images/TankYellow1.png')
tank_image = pygame.transform.scale(tank_image, (34, 43))
player = Player(100, 100)
space_pressed_prev = False
running = True
bullet_list = []
while running:
    screen.blit(back_ground_image, (0, 0))
    player.Print(screen)
    for bullet_index in range(len(bullet_list)):
        if bullet_list[bullet_index].Was_boom is True:
            bullet_list.pop(bullet_index)
        else:
            bullet_list[bullet_index].Update(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.Move_up()
    elif keys[pygame.K_s]:
        player.Move_down()
    elif keys[pygame.K_d]:
        player.Move_right()
    elif keys[pygame.K_a]:
        player.Move_left()
    if keys[pygame.K_SPACE] and space_pressed_prev is False:
        player.Shoot(bullet_list)
        space_pressed_prev = True
    if keys[pygame.K_SPACE] is False:
        space_pressed_prev = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    pygame.display.update()
    clock.tick(15)