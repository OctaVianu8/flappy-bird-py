import sys
import random
import pygame

from bird_obj import BirdObj
from pipe_obj import PipeObj
from sprites import *
from background import Background


# Creating the window
pygame.init()
size = width, height = 800, 800
win = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fps = 24
score = 0

# Constants
BLACK = (0, 0, 0)
PIPE_SPEED = 5
GAP_SIZE = 100

# Importing sprites
bird_downflap = pygame.image.load("assets/sprites/bluebird-downflap.png")
bird_midflap = pygame.image.load("assets/sprites/bluebird-midflap.png")
bird_upflap = pygame.image.load("assets/sprites/bluebird-upflap.png")
score_sprites = {
    '0': pygame.image.load("assets/sprites/0.png"),
    '1': pygame.image.load("assets/sprites/1.png"),
    '2': pygame.image.load("assets/sprites/2.png"),
    '3': pygame.image.load("assets/sprites/3.png"),
    '4': pygame.image.load("assets/sprites/4.png"),
    '5': pygame.image.load("assets/sprites/5.png"),
    '6': pygame.image.load("assets/sprites/6.png"),
    '7': pygame.image.load("assets/sprites/7.png"),
    '8': pygame.image.load("assets/sprites/8.png"),
    '9': pygame.image.load("assets/sprites/9.png"),
}
base = pygame.image.load("assets/sprites/base.png")
pipe = pygame.image.load("assets/sprites/pipe-green.png")

running = True

bird = BirdObj(300,400)

class BaseObj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        win.blit(base, (self.x, self.y))
    
    def move(self):
        self.x -= PIPE_SPEED 


pipes = [PipeObj(500,0,650),PipeObj(800,0,650)]
bases = [BaseObj(0,height-base.get_height()),
    BaseObj(base.get_width(),height-base.get_height()),
    BaseObj(2*base.get_width(),height-base.get_height()),
    BaseObj(3*base.get_width(),height-base.get_height())]

def draw():
    win.fill((0,0,0))
    background.draw()
    bird.draw()
    for pipe_pair in pipes:
        pipe_pair.draw()
    
    for ground in bases:
        ground.draw()
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
    
    global score
    bird_rect = pygame.Rect(bird.x, bird.y, upflap.get_width(), upflap.get_height())
    for pipe_pair in pipes:
        pipe_up_rect = pygame.Rect(pipe_pair.x, pipe_pair.y_up, pipe.get_width(), pipe.get_height())
        pipe_down_rect = pygame.Rect(pipe_pair.x, pipe_pair.y_down, pipe.get_width(), pipe.get_height())

        if bird_rect.colliderect(pipe_up_rect) or bird_rect.colliderect(pipe_down_rect):
            return False
        
        if abs(bird.x - (pipe_pair.x + pipe_down.get_width() / 2) ) <= 3:
            score += 1
            print("caca", score)

    for pipe_pair in pipes:
        if pipe_pair.x + 55 <= 0:
            pipes.remove(pipe_pair)
            new_height = random.randint(-25, 0)
            pipes.append(PipeObj(width + 55, new_height, new_height + GAP_SIZE + pipe_up.get_height()))
    
    for pipe_pair in pipes:
        pipe_pair.move()
    
    for ground in bases:
        if (ground.x + base.get_width() <= 4):
            ground.x = width
    for ground in bases:
        ground.move()
    return True

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.resetSpeed()
        if not logic():
            break
        draw()
        pygame.display.update()
        clock.tick(fps)

pygame.quit()
sys.exit()