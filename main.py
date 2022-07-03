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
backgroundImage = pygame.image.load("assets/sprites/background-day.png")
backgroundImage = pygame.transform.scale(backgroundImage, (400,800))

running = True

bird = BirdObj(300,400)

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

background = Background()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.resetSpeed()

    win.fill((0,0,0))
    background.update()
    background.draw()
    bird.update()
    bird.draw()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()