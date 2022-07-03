import pygame
from constants import *
from sprites import *

# Creating the bird
birdAcceleration = 0.6
fallResetSpeed = -15
maxFallSpeed = 15
maxAscentSpeed = -8

class BirdObj:
    birdFallSpeed = 0
    birdImage = downflap

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        win.blit(self.birdImage, (self.x, self.y))

    def update(self):
        self.y += self.birdFallSpeed
        self.birdFallSpeed += birdAcceleration
        if self.birdFallSpeed > maxFallSpeed :
            self.birdFallSpeed = maxFallSpeed

        if self.birdFallSpeed < 0 :
            self.birdImage = downflap
        elif self.birdFallSpeed > 0 :
            self.birdImage = upflap
        self.updateImage()

    def updateImage(self):
        angle = -self.birdFallSpeed*1.5
        self.birdImage = pygame.transform.rotate(self.birdImage, angle)

    def resetSpeed(self):
        self.birdFallSpeed += fallResetSpeed
        if self.birdFallSpeed < maxAscentSpeed :
            self.birdFallSpeed = maxAscentSpeed
