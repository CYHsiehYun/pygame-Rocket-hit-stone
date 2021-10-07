import pygame
import os
from pygame import sprite
from pygame.constants import QUIT

running = True
FPS = 60 #遊戲每針更新次數
R = 255
G = 255
B = 255
W = 500
H = 600

#init and creat window
pygame.init()
screem = pygame.display.set_mode((W,H))
pygame.display.set_caption("火箭擊石")
clock  = pygame.time.Clock()

#sprite (翻譯:精靈-表物件)
class Player(pygame.sprite.Sprite):#繼承內建(pygame)類別:位置pygame.sprite.Sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)#init
        self.image = pygame.Surface((50,40)) #表圖片
        self.image.fill((0,255,0)) #green
        self.rect = self.image.get_rect() #定位圖片

        self.rect.center = (200,200)

    def update(self):
        self.rect.y += 2

#add all object to sprites groups
all_sprites = pygame.sprite.Group() #群組放sprite物件
player = Player()
all_sprites.add(player)


#main code
while running :
    clock.tick(FPS)
    #input
    for e in pygame.event.get(): # pygame.event.get is a list to show mouse activate
        if e.type == pygame.QUIT:
            running = False

    #update
    all_sprites.update()
    #output
    screem.fill((R,G,B))
    all_sprites.draw(screem)
    pygame.display.update()

pygame.quit()
