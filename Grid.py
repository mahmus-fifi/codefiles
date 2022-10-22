import pygame 
from pygame.locals import * 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RANDOM_COLOR = (122, 200, 125)

WIDTH = 800
HEIGHT = 800

screen_surface = pygame.display.set_mode([WIDTH, HEIGHT], False)
# create a caption 
pygame.display.set_caption('Drawing a Grid')

# fill the screen layer 0
screen_surface.fill(BLACK)

# creating 10 blocks 
def DrawGrid():
    block = 40
    # function to drawlines 
    for i in range (0,WIDTH, block):
        for j in range (0,HEIGHT, block):
            rect = pygame.Rect(i, j, block, block)
            pygame.draw.rect(screen_surface,WHITE,rect,1)
# layer 1
DrawGrid()

def DrawBlock():
    # draws the blocks
    # layer 2 draw squares
    block1 = pygame.Rect(WIDTH//2,40,40,80)
    pygame.draw.rect(screen_surface,RANDOM_COLOR,block1) 



start = True

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False            
        pygame.display.update()
            
pygame.quit()    