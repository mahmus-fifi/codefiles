# basic pygame template to serve as a basis 
# first let's import the pygame module 
import pygame 
from pygame.locals import *
# initialise pygame 
pygame.init()
# creating the WIDTH and HEIGHT for a screen i.e surface 
size = [320, 180]

# let's create a screen 
screen = pygame.display.set_mode(size)

# adding a caption for the title 
pygame.display.set_caption('Boiler Plate')

# change the background color 
COLOR2 = (100,222,120)
COLOR = (255, 255, 255)
COLOR3 = (133, 212, 221)
screen.fill(COLOR2) #ediot, fill first then draw on it, not the other way round
# creating a rect
pygame.draw.rect(screen,COLOR,[50,50,80,50])
# testing the code here will create a window that dissapears
#pygame.draw.rect(screen,COLOR3,[60,50,40,40])
# let's make the window listen for user
start = True
while start:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             start = False
     pygame.display.flip()            
pygame.quit() # uninitialise pygame 
