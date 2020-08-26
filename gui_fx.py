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
        pygame.font.init()
        self.font = pygame.font.SysFont("segoeui", 46)

        # Set the size of game window
        self.screen = pygame.display.set_mode((w, h))

        self.screen.fill(self.backgroundColor)

    def generateBackground(self):
        boxSpacing = self.width/9
        lineThickness = self.width*0.005
        fatlineThickness = self.width*0.01
        offset = -(lineThickness/2)
        fatOffset = -(fatlineThickness/2)
        slimColor = (100,100,100)
        fatColor = (200,200,200)
        
        # Slim lines
        for i in range(10):
            # Horizontal lines
            pygame.draw.rect(self.screen, slimColor, pygame.Rect(offset + i * boxSpacing, 0, lineThickness, self.width))
            # Vertical lines
            pygame.draw.rect(self.screen, slimColor, pygame.Rect(0, offset+ i * boxSpacing, self.width, lineThickness))

        # Thicc lines
        for i in range(4):
            # Horizontal lines
            pygame.draw.rect(self.screen, fatColor, pygame.Rect(fatOffset + i * (boxSpacing*3), 0, fatlineThickness, self.width))
            # Vertical lines
            pygame.draw.rect(self.screen, fatColor, pygame.Rect(0, fatOffset+ i * (boxSpacing*3), self.width, fatlineThickness))

    def drawDigits(self, mtx):
        spacing = self.width/9
        horizontalOffset = spacing/2

        for row in range(9):
            for col in range(9):
                if mtx[row][col] != 0:
                    text = self.font.render(str(mtx[row][col]), True, (120, 20, 150))
                    self.screen.blit(text,
                    (spacing * col + horizontalOffset - (text.get_width()/2), 
                    spacing * row))
        

        

    