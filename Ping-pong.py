from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.player_speed
        if keys_pressed[K_s] and self.rect.y < 490:
            self.rect.y += self.player_speed
    
    def update_r(self):
        key = key.get_pressed()
        if key[K_UP] and self.rect.y > 10:
            self.rect.y -= self.player_speed
        if keys_pressed[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.player_speed
