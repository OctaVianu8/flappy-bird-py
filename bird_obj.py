import pygame

birdUpImage = pygame.image.load("assets/sprites/bluebird-downflap.png")
birdDownImage = pygame.image.load("assets/sprites/bluebird-upflap.png")

# Creating the bird
birdAcceleration = 0.6
fallResetSpeed = -15
maxFallSpeed = 15
maxAscentSpeed = -8
size = width, height = 800, 800
win = pygame.display.set_mode(size)

class BirdObj:
    birdFallSpeed = 0
    birdImage = birdUpImage

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
