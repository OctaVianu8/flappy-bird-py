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

# Creating the bird
birdImage = pygame.image.load("assets/sprites/bluebird-midflap.png")
birdAcceleration = 0.5
fallResetSpeed = -5

class BirdObj:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.birdFallSpeed = 0
        
    def draw(self):
        win.blit(birdImage, (self.x, self.y))

    def update(self):
        self.y += self.birdFallSpeed
        self.birdFallSpeed += birdAcceleration

    def resetSpeed(self):
        bird.birdFallSpeed = fallResetSpeed

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