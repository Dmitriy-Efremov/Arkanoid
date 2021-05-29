import pygame
from random import randint

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,speed_y,speed_x, size_x, size_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self,center,radius,ball_x, ball_y, speed_y, speed_x):
        self.center = center
        self.radius = radius
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.ball_x += self.speed_x
        self.ball_y -= self.speed_y
        if self.ball_x >= 690 or self.ball_x <= 0:
            self.speed_x = self.speed_x * -1
        if self.ball_y >= 490 or self.ball_y <=0:
            self.speed_y = self.speed_y * -1
        if player.colliderect(ball):
            ball.speed_x = ball.speed_x * -1
    '''def reset(self):
        pygame.Rect(12, 20, 800, 700)
        pygame.draw.circle(window,(0,0,0),(self.ball_x, self.ball_y), self.radius)'''


window = pygame.display.set_mode((700,500))

clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("background.png").convert()

pygame.font.init()
font2 = pygame.font.SysFont('Arial', 36)
player = pygame.Rect(300,400,200,50)
ball = pygame.Rect(450, 350, 20, 20)
#ball = Ball(20,15,300,400,6,6)
#ball = pygame.Rect(12,20,800,700)
ball_speed_x = 6
ball_speed_y = 6
blocks = []
for i in range(10):
    for j in range(4):
        block = pygame.Rect(1 + 88 * i, 1 + 60 * j, 85, 50)
        blocks.append(block)
        print(blocks)
finish = False
game = True

pygame.font.init()
font2 = pygame.font.SysFont('Arial', 36)

while game:
    if not finish:
        print(len(blocks))
        window.blit(background, (0, 0))
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and player.x >= 5:
            player.x -= 8
        if keys_pressed[pygame.K_RIGHT] and player.x <= 495:
            player.x += 8
        pygame.draw.rect(window,(255,0,255), player)
        for block in blocks:
            if ball.colliderect(block):
                blocks.remove(block)
                ball_speed_y = ball_speed_y * -1
            pygame.draw.rect(window, (0,255,0), block)
        pygame.draw.circle(window,(0,0,0), (ball.x,ball.y), 10)
        ball.x += ball_speed_x
        ball.y += ball_speed_y * -1
        if ball.x <= 0 or ball.x >= 700:
            ball_speed_x = ball_speed_x * -1
        if ball.y <= 0:
            ball_speed_y = ball_speed_y * -1
        if player.colliderect(ball):
            ball_speed_y = ball_speed_y * -1
        if ball.collidelist(blocks):
            ball_speed_y = ball_speed_y * -1
        if ball.collidelist(blocks):
            ball_speed_y = ball_speed_y * -1
        if ball.y >= 500:
            lose = font2.render("Вы проиграли!", 1, (200, 215, 0))
            window.blit(lose, (200, 250))
            finish = True
        if len(blocks) == 4:
            win = font2.render("Вы выиграли!", 1, (200, 215, 0))
            window.blit(win, (200, 250))
            finish = True
    else:
        ball.x = 450
        ball.y = 350
        ball.x += ball_speed_x
        ball.y += ball_speed_y * -1
        finish = False
        pygame.time.delay(3000)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(FPS)