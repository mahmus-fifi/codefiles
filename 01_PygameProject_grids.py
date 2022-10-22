import pygame 
import random 
from pygame.locals import * 
__author__ = 'Mahmud Shuaib daddy mimi hubby fifi'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# set of random colors 
RANDOM_BG_COLOR =    (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_2 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_3 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_4 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_5 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_6 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_7 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_8 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_9 =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_10 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RANDOM_BG_COLOR_11 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
# Screen Size 
WIDTH = 480
HEIGHT = 480
# creating the display surface aka window 
screen_surface = pygame.display.set_mode([WIDTH, HEIGHT], False)
# create a caption 
pygame.display.set_caption('Drawing a Grid')
velocity = 10
# fill the screen layer 0
screen_surface.fill(BLACK)
# creating 10 blocks 
def DrawGrid():
    block = 40
    # function to drawlines 
    for i in range (0,WIDTH, block):
        for j in range (0,HEIGHT, block):
            rect = pygame.Rect(i, j, block, block)
            pygame.draw.rect(screen_surface,RANDOM_BG_COLOR,rect,1)
# layer 1
DrawGrid()
def DrawBlock():
    # draws the blocks
    # layer 2 draw squares
    block1 = pygame.Rect(40,40,40,80)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_2,block1) 
    
    block2 = pygame.Rect(40,120,80,40)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_3,block2)
    
    block3 = pygame.Rect(120,80,120,120)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_4,block3)
    
    block4 = pygame.Rect(240,120,80,40)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_5,block4)
    
    block5 = pygame.Rect(280,160,40,80)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_6,block5)
    
    block6 = pygame.Rect(160,200,40,80)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_7,block6)
    
    block7 = pygame.Rect(120,280,120,40)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_8,block7)
    
    block8 = pygame.Rect(160,320,40,40)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_9,block8)
    
    block9 = pygame.Rect(80,360,200,40)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_10,block9)
    
    block10 = pygame.Rect(240,400,40,40)
    pygame.draw.rect(screen_surface,RANDOM_BG_COLOR_11,block10)       
# layer 2
# DrawBlock
DrawBlock()
start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False            
        pygame.display.update()
        # future stuff 
        # key controls 
        # move the block        
# exit program             
pygame.quit()    


