import pygame, sys,os
from pygame.locals import * 
 
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
         print (5)
 
while True: 
   input(pygame.event.get())
