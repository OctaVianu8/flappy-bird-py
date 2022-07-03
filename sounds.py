import pygame 

pygame.init()
dj = pygame.mixer
wing_sound = dj.Sound("assets/audio/wing.wav")
point_sound = dj.Sound("assets/audio/point.wav")
hit_sound = dj.Sound("assets/audio/hit.wav")
die_sound = dj.Sound("assets/audio/die.wav")