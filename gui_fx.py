import pygame
from pygame.locals import *

#pygame.rect (x,y,w,h)

class GUI:
    def __init__(self, w:int, h:int):
        self.width = w
        self.height = h
        self.state = True
        # Initiate the pygame engine
        pygame.init()

        # Set the size of game window
        self.screen = pygame.display.set_mode((w, h))
        self.screen.fill((25,25,25)) # 2x parentheses bcs the arg= color