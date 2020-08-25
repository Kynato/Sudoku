# IMPORTS
from gui_fx import *

# Game window dimensions
WINDOW_WIDTH = WINDOW_HEIGHT = 600


# gui will be our graphics manager
gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT)
gui.generateBackground()

while gui.state:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gui.state = False
        #pygame.draw.rect(gui.screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()