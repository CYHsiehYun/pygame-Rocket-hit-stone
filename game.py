import pygame
import os

from pygame.constants import QUIT


#init and creat window


running = True
FPS = 60 #遊戲每針更新次數
R = 255
G = 255
B = 255
W = 500
H = 600

pygame.init()
screem = pygame.display.set_mode((W,H))
clock  = pygame.time.Clock()


#game alive
while running :
    clock.tick(FPS) #ruturn a num
    #input
    for e in pygame.event.get(): #return a list to show mouse activate
        if e.type == pygame.QUIT:
            running = False

    #update

    #output
    screem.fill((R,G,B))
    pygame.display.update()

pygame.quit()
