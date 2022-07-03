import pygame
from sprites import *
from constants import *

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
