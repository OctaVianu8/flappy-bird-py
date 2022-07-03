import sys
import random
import pygame
import time

from bird_obj import BirdObj
from pipe_obj import PipeObj
from base_obj import BaseObj
from sprites import *
from constants import *
from sounds import *
from background import Background


# Creating the window
pygame.init()
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
score = 0

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

print("ma pis pe python")

bird = BirdObj(300,400)
background = Background()
pipes = [PipeObj(500,0,650),PipeObj(800,0,650)]
bases = [BaseObj(0,HEIGHT-BASE_HEIGHT),
    BaseObj(base.get_width(),HEIGHT-BASE_HEIGHT),
    BaseObj(2*base.get_width(),HEIGHT-BASE_HEIGHT),
    BaseObj(3*base.get_width(),HEIGHT-BASE_HEIGHT)]

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
        win.blit(score_sprites[str(digit)], (WIDTH - score_width - 50, 50))
        score_width -= score_sprites[str(digit)].get_width()
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
    bird_rect = pygame.Rect(bird.x, bird.y, upflap.get_width(), BIRD_HEIGHT)
    for pipe_pair in pipes:
        pipe_up_rect = pygame.Rect(pipe_pair.x, pipe_pair.y_up, pipe.get_width(), PIPE_HEIGHT)
        pipe_down_rect = pygame.Rect(pipe_pair.x, pipe_pair.y_down, pipe.get_width(), PIPE_HEIGHT)

        if bird_rect.colliderect(pipe_up_rect) or bird_rect.colliderect(pipe_down_rect):
            hit_sound.play()
            time.sleep(0.5)
            return False
        
        if abs(bird.x - (pipe_pair.x + pipe_down.get_width() / 2) ) <= 3:
            score += 1
            point_sound.play()
            print("caca", score)

    for pipe_pair in pipes:
        if pipe_pair.x + 55 <= 0:
            pipes.remove(pipe_pair)
            new_height = random.randint(-25, 0)
            pipes.append(PipeObj(WIDTH + 55, new_height, new_height + GAP_SIZE + PIPE_HEIGHT))
    
    for pipe_pair in pipes:
        pipe_pair.move()
    
    for ground in bases:
        ground_rect = pygame.Rect(ground.x, ground.y, base.get_width(), BASE_HEIGHT)

        if bird_rect.colliderect(ground_rect):
            hit_sound.play()
            time.sleep(0.5)
            return False
    for ground in bases:
        if (ground.x + base.get_width() <= 4):
            ground.x = WIDTH
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
            if event.type == pygame.MOUSEBUTTONUP:
                wing_sound.play()
                bird.resetSpeed()
        if not logic():
            break
        draw()
        pygame.display.update()
        clock.tick(FPS)

pygame.quit()
sys.exit()