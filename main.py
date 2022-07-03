from cProfile import run
import sys
import random
import pygame
import time

from bird_obj import *
from pipe_obj import *
from base_obj import *
from sprites import *
from constants import *
from sounds import *
from background import Background


# Creating the window
pygame.init()
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

score = 0

bird = BirdObj(birdX,400)

class BaseObj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        win.blit(base, (self.x, self.y))
    
    def move(self):
        self.x -= PIPE_SPEED 

high_score = 0

pipes = []
bases = []

def get_high_score():
    f = open("highscore.txt", "r")
    num = int(f.read())
    return num

def update_high_score():
    if score > high_score:
        with open('highscore.txt','w') as f:
            f.write(str(score))

def initialize():
    global score, high_score
    score = 0
    high_score = get_high_score()
    print(high_score)
    pipes.clear()
    bases.clear()
    bird.y=400
    bird.birdFallSpeed=0
    draw()
    for i in range(2,5):
        new_height = random.randint(-280, 0)
        pipes.append(PipeObj(300*i,new_height,new_height + GAP_SIZE + PIPE_HEIGHT))
    for i in range(4):
        bases.append(BaseObj(i*BASE_WIDTH, HEIGHT-BASE_HEIGHT))
    
background = Background()

def draw_number(num, x, y):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    if len(digits) == 0: digits.append(0)
    digits.reverse()

    num_width = 0
    for digit in digits:
        num_width += score_sprites[str(digit)].get_width()
    
    for digit in digits:
        win.blit(score_sprites[str(digit)], (x - num_width, y))
        num_width -= score_sprites[str(digit)].get_width()

def draw():
    win.fill((0,0,0))
    background.draw()
    bird.draw()
    for pipe_pair in pipes:
        pipe_pair.draw()
    
    for ground in bases:
        ground.draw()

    draw_number(score, WIDTH - 50, 50)
    return

def logic():
    background.update()
    bird.update()
    
    # Sky collision
    if bird.y + BIRD_HEIGHT / 2 <= 0:
        hit_sound.play()
        time.sleep(0.5)
        return False

    global score
    bird_rect = pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
    for pipe_pair in pipes:
        pipe_up_rect = pygame.Rect(pipe_pair.x, pipe_pair.y_up, PIPE_WIDTH, PIPE_HEIGHT)
        pipe_down_rect = pygame.Rect(pipe_pair.x, pipe_pair.y_down, PIPE_WIDTH, PIPE_HEIGHT)

        if bird_rect.colliderect(pipe_up_rect) or bird_rect.colliderect(pipe_down_rect):
            hit_sound.play()
            time.sleep(0.5)
            return False
        
        if abs(bird.x - (pipe_pair.x + PIPE_WIDTH / 2) ) <= 3:
            score += 1
            point_sound.play()

    for pipe_pair in pipes:
        if pipe_pair.x + PIPE_WIDTH <= 0:
            pipes.remove(pipe_pair)
            new_height = random.randint(-280, 0)
            pipes.append(PipeObj(WIDTH + PIPE_WIDTH, new_height, new_height + GAP_SIZE + PIPE_HEIGHT))
    
    for pipe_pair in pipes:
        pipe_pair.move()

    for ground in bases:
        ground_rect = pygame.Rect(ground.x, ground.y, BASE_WIDTH, BASE_HEIGHT)

        if bird_rect.colliderect(ground_rect):
            hit_sound.play()
            time.sleep(0.5)
            return False
    for ground in bases:
        if (ground.x + BASE_WIDTH <= 4):
            ground.x = WIDTH
    for ground in bases:
        ground.move()
    return True

def draw_start_screen():
    draw_number(high_score, 400, 250)

while True :
    initialize()
    draw_start_screen()
    pygame.display.update()

    running = False
    while running == False :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
            if event.type == pygame.MOUSEBUTTONUP:
                running = True
        
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    wing_sound.play()
                    bird.resetSpeed()
            if event.type == pygame.MOUSEBUTTONUP:
                wing_sound.play()
                bird.resetSpeed()
        if not logic():
            break
        draw()
        pygame.display.update()
        clock.tick(FPS)
    
    running = False
    update_high_score()

pygame.quit()
sys.exit()