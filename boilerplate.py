# basic pygame template to serve as a basis 
# first let's import the pygame module 
import pygame 
# initialise pygame 
pygame.init()
# creating the WIDTH and HEIGHT for a screen i.e surface 
size = [320, 180]

# let's create a screen 
screen = pygame.display.set_mode(size)

# adding a caption for the title 
pygame.display.set_caption('Boiler Plate')

# testing the code here will create a window that dissapears

# let's make the window listen for user
start = True
while start:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             start = False
             
pygame.quit() # uninitialise pygame 

        




