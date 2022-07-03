import pygame
from sprites import *


size = width, height = 800, 800
win = pygame.display.set_mode(size)

class Background:
    backgroundSpeed = -1
    x = [0,400,800]

    def __init__(self) : None

    def draw(self) :
        for i in range(3) : 
            win.blit(backgroundImage, (self.x[i], 0))

    def update(self) :
        for i in range(3) : 
            self.x[i] += self.backgroundSpeed
            if self.x[i] < -400 : self.x[i] +=1200