from pygame import *
font.init()

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.player_speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.player_speed
        if keys[K_s] and self.rect.y < 370:
            self.rect.y += self.player_speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.player_speed
        if keys[K_DOWN] and self.rect.y < 370:
            self.rect.y += self.player_speed

window = display.set_mode((600, 500))
window.fill((116, 243, 253))

p1 = Player('ракетка.png', -10, 200, 5, 70, 140)
p2 = Player('ракетка 2.png', 540, 200, 5, 70, 140)
ball = GameSprite('мячик.png', 270, 250, 4, 50, 50)

speed_x = 4
speed_y = 2
clock = time.Clock()
FPS = 60
game = True
finish = False
font1 = font.SysFont('Arial', 50)
p1_lose = font1.render('PLAYER 1 LOSE!!!', True, (217, 39, 0))
p2_lose = font1.render('PLAYER 2 LOSE!!!', True, (217, 39, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((116, 243, 253))
        p1.reset()
        p2.reset()
        ball.reset()
        p1.update_l()
        p2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 10 or ball.rect.y > 460:
            speed_y *= -1
        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(p1_lose, (150, 200))
        if ball.rect.x > 500:
            finish = True
            window.blit(p2_lose, (150, 200))
    display.update()
    clock.tick(FPS)
