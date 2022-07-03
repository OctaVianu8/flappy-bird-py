from cProfile import run
import sys
import random
import pygame

from bird_obj import BirdObj
from pipe_obj import *
from sprites import *
from background import Background

# Creating the window
pygame.init()
size = width, height = 800, 800
win = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fps = 24
score =0
birdX = 250

# Constants
BLACK = (0, 0, 0)
PIPE_SPEED = 5
GAP_SIZE = 150

running = True

bird = BirdObj(birdX,400)

class BaseObj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        win.blit(base, (self.x, self.y))
    
    def move(self):
        self.x -= PIPE_SPEED 


pipes = []
bases = []

def initialize():
    draw()
    for i in range(2,5):
        new_height = random.randint(-280, 0)
        pipes.append(PipeObj(300*i,new_height,new_height + GAP_SIZE + pipeHeight))
    for i in range(4):
        bases.append(BaseObj(i*base.get_width(),height-base.get_height()))
    

def draw():
    win.fill((0,0,0))
    background.draw()
    bird.draw()
    for pipe_pair in pipes:
        pipe_pair.draw()
    
    for ground in bases:
        ground.draw()
    #draw score
    tmp = score
    digits = []
    while tmp > 0:
        digits.append(tmp % 10)
        tmp //= 10
    if len(digits) == 0: digits.append(0)
    digits.reverse()

    score_width = 0
    for digit in digits:
        score_width += score_sprites[str(digit)].get_width()

    for digit in digits:
        win.blit(score_sprites[str(digit)], (width - score_width - 50, 50))
        score_width -= score_sprites[str(digit)].get_width()
    return

background = Background()

def logic():
    background.update()
    bird.update()
    for pipe_pair in pipes:
        if pipe_pair.x + pipeWidth <= 0:
            pipes.remove(pipe_pair)
            new_height = random.randint(-280, 0)
            pipes.append(PipeObj(width + pipeWidth, new_height, new_height + GAP_SIZE + pipe_up.get_height()))
    
    for pipe_pair in pipes:
        pipe_pair.move()
    
    for ground in bases:
        if (ground.x + base.get_width() <= 4):
            ground.x = width
            
    for ground in bases:
        ground.move()
    return

while True :
    initialize()

    running = False
    while running == False :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
    
    while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.resetSpeed()
            logic()
            draw()
            pygame.display.update()
            clock.tick(fps)

pygame.quit()
sys.exit()