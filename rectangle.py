import pygame, sys,os
from pygame.locals import * 

red = ( 255, 0, 0)
white = ( 255, 255, 255)
 
pygame.init() 
 
window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("PythonRectangleYo")
screen = pygame.display.get_surface()

done=False

x_position = 50
y_position = 50
direction = (1, 0)
clock=pygame.time.Clock()

while done==False:
    screen.fill(red)
    pygame.draw.rect(screen,white,[x_position, y_position, 20, 20])
    pygame.display.flip()

    x_position = x_position + 5*direction[0]
    y_position = y_position + 5*direction[1]

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP:
            if event.dict["key"] == pygame.K_UP:
                direction = (0, -1)
            if event.dict["key"] == pygame.K_DOWN:
                direction = (0, 1)
            if event.dict["key"] == pygame.K_RIGHT:
                direction = (1, 0)
            if event.dict["key"] == pygame.K_LEFT:
                direction = (-1, 0)
pygame.quit()

