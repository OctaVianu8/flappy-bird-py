import sys
import random
import pygame

from bird_obj import BirdObj

# Creating the window
pygame.init()
size = width, height = 800, 800
win = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fps = 24

running = True

bird = BirdObj(300,400)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.resetSpeed()

    win.fill((0,0,0))
    bird.update()
    bird.draw()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()