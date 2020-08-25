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

    def generateBackground(self):
        boxSize = self.width/9
        barColor = (0,0,0)
        # vBar - Vertical bar
        # hBar - Horizontal bar
        vBar = pygame.Rect(0, 0, 3, self.width)
        
        for i in range(10):
            pygame.draw.rect(self.screen, barColor, pygame.Rect(i * boxSize, 0, self.width*0.005, self.width))
            pygame.draw.rect(self.screen, barColor, pygame.Rect(0, i * boxSize, self.width, self.width*0.005))

