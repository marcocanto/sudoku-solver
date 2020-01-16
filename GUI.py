import pygame
import time
from sudoku import solve, valid
pygame.font.init()
from sys import exit

class Grid:
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

    seafoam = (220, 255, 220)
    black = (200, 235 ,200)
    lack = (180,205,180)


    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cube = [[Cube(self.board[i][j], i, j, width, height) \
            for j in range(cols)] for i in range(rows)]
        self.width = width 
        self.height = height
        self.model = None
        self.select = None

    def draw_square(self, win):
        color = True
        for x in range(3):
            for y in range(3):
                if color:
                    pygame.draw.rect(win, self.seafoam,(x * 180,y * 180, 180, 180))
                    color = False
                else: 
                    pygame.draw.rect(win, self.black,(x * 180, y * 180, 180, 180))
                    color = True

    def draw_lines(self, win):
        #vertical 
        for line in range(0, 10):
            if line % 3 == 0:
                pygame.draw.line(win, (0,0,0), (60 * line, 0),(60 * line, 540), 3)
            else:
                pygame.draw.line(win, (0,0,0), (60 * line, 0),(60 * line, 540), 2)
        #horizontal
        for line in range(0, 10):
            if line % 3 == 0:
                pygame.draw.line(win, (0,0,0), (0, 60 * line),(540, 60 * line), 3)
            else:
                pygame.draw.line(win, (0,0,0), (0, 60 * line),(540, 60 * line), 2)

    
    def draw(self, win):
        self.draw_square(win)
        self.draw_lines(win)
        for cube in self.cubes:
            cube.draw(win)


        

def Cube(num, row, col, width, height):
    def __init__():
        self.num = num
        self.row = row
        self.col = col
        self.width = width 
        self.height = height
        self.model = None
        self.select = None
    
    def draw(self, win):
        

def redraw_window(win, board, time):
    win.fill((180,205,180))
    fnt = pygame.font.SysFont("comicsans", 40, bold=True, italic=False)
    text = fnt.render("Time:" + str(time), 1 , (0,0,0))
    win.blit(text, (540 - 160, 560))
    board.draw(win)


def main():
    board = Grid(9,9, 540, 540)
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    key = None
    run = True
    start = time.time()
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        redraw_window(win, board, play_time)
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()

main()