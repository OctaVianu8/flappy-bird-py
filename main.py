import sys
import random
import pygame

# Creating the window
pygame.init()
size = width, height = 800, 800
win = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fps = 24

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()