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
birdUpImage = pygame.image.load("assets/sprites/bluebird-downflap.png")
birdDownImage = pygame.image.load("assets/sprites/bluebird-upflap.png")
birdAcceleration = 0.5
fallResetSpeed = -15
maxFallSpeed = 15
maxAscentSpeed = -8

class BirdObj:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.birdFallSpeed = 0
        self.birdImage = birdUpImage
        
    def draw(self):
        win.blit(self.birdImage, (self.x, self.y))

    def update(self):
        self.y += self.birdFallSpeed
        self.birdFallSpeed += birdAcceleration
        if self.birdFallSpeed > maxFallSpeed :
            self.birdFallSpeed = maxFallSpeed

        if self.birdFallSpeed < 0 :
            self.birdImage = birdUpImage
        elif self.birdFallSpeed > 0 :
            self.birdImage = birdDownImage
        self.updateImage()

    def updateImage(self):
        angle = -self.birdFallSpeed*1.5
        self.birdImage = pygame.transform.rotate(self.birdImage, angle)

    def resetSpeed(self):
        self.birdFallSpeed += fallResetSpeed
        if self.birdFallSpeed < maxAscentSpeed :
            self.birdFallSpeed = maxAscentSpeed

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