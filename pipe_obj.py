import pygame
from sprites import *

size = width, height = 800, 800
win = pygame.display.set_mode(size)

# Constants
BLACK = (0, 0, 0)
PIPE_SPEED = 5
GAP_SIZE = 100

class PipeObj:
    def __init__(self, x, y_up, y_down):
        self.x = x
        self.y_up = y_up
        self.y_down = y_down
        
    
    def draw(self):
        win.blit(pipe_down, (self.x, self.y_down))
        win.blit(pipe_up, (self.x, self.y_up))
    
    def move(self):
        self.x -= PIPE_SPEED
