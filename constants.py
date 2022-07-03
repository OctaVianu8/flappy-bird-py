import pygame
from sprites import *

# Constants
BLACK = (0, 0, 0)
PIPE_SPEED = 5
GAP_SIZE = 100
FPS = 24
SIZE = WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode(SIZE)
BASE_HEIGHT = base.get_height()
BASE_WIDTH = base.get_width()
PIPE_HEIGHT = pipe_up.get_height()
PIPE_WIDTH = pipe_up.get_width()
BIRD_HEIGHT = upflap.get_height()
BIRD_WIDTH = upflap.get_width()