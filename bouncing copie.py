import pygame, sys,os
from pygame.locals import * 

red = ( 255, 0, 0)
white = ( 255, 255, 255)
 
pygame.init() 
 
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("PythonRectangleYo")

done = False

clock=pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5


screen.fill(red)

pygame.draw.rect(screen,white,[rect_x,rect_y,20,20])
rect_x += rect_change_x
rect_y += rect_change_y

if rect_y > 300 or rect_y < 0:
    rect_change_y = rect_change_y * -1
if rect_x > 300 or rect_x < 0:
    rect_change_x = rect_change_x * -1




            
clock.tick(20)


pygame.display.flip()


pygame.quit()

