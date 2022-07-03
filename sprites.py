import pygame

downflap = pygame.image.load("assets/sprites/bluebird-downflap.png")
upflap = pygame.image.load("assets/sprites/bluebird-upflap.png")
downflap = pygame.transform.scale(downflap,(40,40))
upflap = pygame.transform.scale(upflap,(40,40))

pipe_down = pygame.image.load("assets/sprites/pipe-green.png")
pipeWidth = 80
pipeHeight = 400
pipe_down = pygame.transform.scale(pipe_down, (80,400))
pipe_up = pygame.transform.rotate(pipe_down, 180)
base = pygame.image.load("assets/sprites/base.png")
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
backgroundImage = pygame.image.load("assets/sprites/background-day.png")
backgroundImage = pygame.transform.scale(backgroundImage, (400,800))