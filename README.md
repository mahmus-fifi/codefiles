# Program That Displays Blocky Shapes on a Grid :cd:

written by Mahmud K. Shuaib
mail: 101touchapps@gmail.com

Hi there, this program is a fun project that display blocks on a grid using **pygame**.
pygame is a graphics and multimedia library written using SDL (Simple Direct Layer). It allows
the user to use highlevel functionality by granting access to input devices and hardware such as keyboards, joystics, mouse, audio, graphic and text. You can findout more about pygame here: [pygame website](https://www.pygame.org/docs/)

![img1](https://i.imgur.com/6HnWz3O.png "screen shot of the grid program")
screenshot of the program

# 2 Downloading and Installing Python :snake:

To follow this tutorial you should have a copy of Python and pygame installed. To download Python, Headover to
<https://www.python.org> and download Python for your operating system.
![img2](https://i.imgur.com/o7mlY6m.png "image showing pythons webpage")
image showing pythons splash page

# 3 Installing Pygame :video_game:

To install pygame open a **Terminal** on Mac or command prompt on **PC** and type `pip install pygame` note, you need to have an active internet connection because the pip command will connect to [pypi](https://www.pypi.org) to get the latest version of pygame.

# 4. Importing pygame and Creating Variables

once you have installed python open up your editor and create a new python file. some editor options to use are

1. Sublime Text3 Editor -  ***[Sublime](https://www.sublimetext.com/3)***
2. Visual Studio Code- ***[vs code](https://code.visualstudio.com/)***
3. Atom - ***[Atom](https://flight-manual.atom.io/getting-started/sections/installing-atom/)***
4. IDLE, Integrated Development and Learning Environment.
**NOTE**
IDLE comes built into python, just search for IDLE on your computer and you are all setup.

# 5 Our Program Structure

Here is the full version of the program
You can find it here: <>

``` python
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




```
