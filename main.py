# IMPORTS
from functions import Sudoku, fillPretendents
from gui_fx import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
clock = pygame.time.Clock()

# gui will be our graphics manager
gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT)
#gui.generateBackground()

# Declaration of sudoku board
Board = [   [2, 0, 0,   0, 3, 1,    0, 0, 6],
            [5, 0, 7,   4, 0, 8,    2, 3, 9],
            [0, 6, 0,   0, 0, 0,    4, 0, 7],

            [3, 4, 0,   2, 5, 0,    0, 0, 0],
            [0, 8, 1,   0, 0, 0,    6, 2, 5],
            [6, 5, 0,   0, 0, 7,    0, 4, 0],

            [9, 2, 0,   1, 7, 3,    0, 6, 4],
            [1, 0, 5,   6, 8, 0,    7, 0, 2],
            [4, 7, 0,   0, 2, 5,    3, 0, 0]]

# TESTS
#print(pygame.font.get_fonts())

# Transform a matrice into sudoku class
S1 = Sudoku(Board)
S1.printBoard()
gui.render(S1.rows)
gui.drawButtons()




#S1.solve()
'''
while S1.isSolved() == False:
    fillPretendents(S1)
    gui.render(S1.rows)
    pygame.display.flip()
    pygame.time.wait(1000)'''


S1.printBoard()

while gui.state:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gui.state = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        # 1 is the left mouse button, 2 is middle, 3 is right.
                        if event.button == 1:
                                # `event.pos` is the mouse position.
                                if gui.whichButton(event.pos) == 0:
                                        S1.solve()
                                        gui.render(S1.rows)
                                        pygame.display.flip()
                                elif gui.whichButton(event.pos) == 1:
                                        gui.state = False
        pygame.display.flip()
