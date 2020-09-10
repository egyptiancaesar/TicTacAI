import os
import sys
import time
import warnings
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import pygame as pg
from pygame.locals import *

#global variables
XO = 'X' #for knowing whos turn it is
width = 400
height = 400
white = (255, 255, 255) #white for boxes
line_color = (0, 0 , 0) #black for lines
in_draw = None  #whether the game has ended in a draw or not
winner = None

#this can be more modular
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0 , 32)
pg.display.set_caption("Tic Tac Hoe")
init_window = pg.image.load("Resources/cover.png")
x_img = pg.image.load("Resources/x.png")
o_img = pg.image.load("Resources/o.png")
init_window = pg.transform.scale(init_window, (width, height +100))
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))

def game_init_window():
    screen.blit(init_window, (0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    # drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    global in_draw
    if winner is None:
        message = XO.upper() + "'s Turn."
    else:
        message = winner.upper() + " Won!"
    if in_draw:
        message = "Draw Game!"
    font = pg.font.Font(None, 30) 
      
    # setting the font properties like  
    # color and width of the text 
    text = font.render(message, 1, (255, 255, 255)) 
   
    # copy the rendered message onto the board 
    # creating a small block at the bottom of the main display 
    screen.fill ((0, 0, 0), (0, 400, 500, 100)) 
    text_rect = text.get_rect(center =(width / 2, 500-50)) 
    screen.blit(text, text_rect) 
    pg.display.update() 

game_init_window()
