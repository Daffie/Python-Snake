import pygame, sys,os
from pygame.locals import * 

red = ( 255, 0, 0)
white = ( 255, 255, 255)
 
pygame.init() 
 
window = pygame.display.set_mode((468, 400)) 
pygame.display.set_caption('Pysnakeyo') 
screen = pygame.display.get_surface() 

pygame.display.flip()

 
def input(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
      else:
         rect_x = 50
         pygame.draw.rect(window,white,[rect_x,20,20,20])

 
while True: 
    input(pygame.event.get()
          rect_x += 5
