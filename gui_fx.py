import pygame
from pygame.locals import *

#pygame.rect (x,y,w,h)

class GUI:
    def __init__(self, w:int, h:int):
        self.width = w
        self.height = h
        self.state = True
        self.backgroundColor = pygame.Color(25, 25, 25)
        # Initiate the pygame engine
        pygame.init()

        # Set the size of game window
        self.screen = pygame.display.set_mode((w, h))

        self.screen.fill(self.backgroundColor)

    def generateBackground(self):
        boxSize = self.width/9
        lineThickness = self.width*0.005
        offset = -(lineThickness/2)
        barColor = (5,5,5)
        # vBar - Vertical bar
        # hBar - Horizontal bar
        vBar = pygame.Rect(0, 0, 3, self.width)
        
        for i in range(10):
            # Horizontal lines
            pygame.draw.rect(self.screen, barColor, pygame.Rect(offset + i * boxSize, 0, lineThickness, self.width))
            # Vertical lines
            pygame.draw.rect(self.screen, barColor, pygame.Rect(0, offset+ i * boxSize, self.width, lineThickness))

