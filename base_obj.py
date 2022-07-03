import pygame
from sprites import *
from constants import *

class BaseObj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        win.blit(base, (self.x, self.y))
    
    def move(self):
        self.x -= PIPE_SPEED 