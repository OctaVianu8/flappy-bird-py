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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()