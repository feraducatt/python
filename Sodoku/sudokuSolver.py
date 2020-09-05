import pygame
from random import randint, shuffle
import sys
from time import sleep

puzzle = []
for i in range(0,9):
    puzzle.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
numbers = list(range(1, 10))
blankSpaces = []

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
colInact = pygame.Color('black')
#colActive = pygame.Color('black')
main_font = pygame.font.SysFont('times new roman', 30)

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0, 0, 0)
        self.text = text
        self.txt_surface = main_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = colInact if self.active else colInact
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = main_font.render(self.text, True, self.color)

    #def update(self):
        # Resize the box if the text is too long.
     #   width = max(200, self.txt_surface.get_width()+10)
      #  self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        #pygame.draw.rect(screen, self.color, self.rect, 2)

def drawPuzzle(puzzle):
    x_start = 80
    y_start = 80
    dim = 40
    for row in range(0, 10):
        if (row % 3) == 0:
            width = 3
        else:
            width = 1
        pygame.draw.line(screen, (0,0,0), (x_start, (y_start+row*dim)), (x_start+9*dim, y_start+row*dim), width)
    for col in range(0,10):
        if (col % 3) == 0:
            width = 3
        else:
            width = 1
        pygame.draw.line(screen, (0,0,0), (x_start+col*dim, y_start), (x_start+col*dim, y_start+9*dim), width)
    for row in range(0,9):
        for col in range(0,9):
            if (puzzle[row][col] == 0):
                blankSpaces.append(InputBox(x_start+col*dim+5,y_start+row*dim,dim,dim))
            else:
                writeText(str(puzzle[row][col]), int(x_start+col*dim+dim*.5-6), int(y_start+row*dim-dim*.5+25))

def writeText(text, x, y):
    num = main_font.render(text, True, (0,0,0))
    screen.blit(num, (x, y))

def checkPuzzleComplete(puzzle):
    for row in range(0,9):
        for col in range(0,9):
            if puzzle[row][col] == 0:
                return False
    return True

def allRows(puzzle, col):
    values=[]
    for i in range(0,9):
        values.append(puzzle[i][col])
    return values

def makePuzzle(puzzle):
    for i in range(0,81):
        row = i // 9
        col = i % 9
        if puzzle[row][col] == 0:
            shuffle(numbers)
            for number in numbers:
                if not(number in puzzle[row]):
                    if not(number in (
                    puzzle[0][col], puzzle[1][col], puzzle[2][col], puzzle[3][col], puzzle[4][col], puzzle[5][col], puzzle[6][col],
                    puzzle[7][col], puzzle[8][col])):
                        if row < 3:
                            if col < 3:
                                square = [puzzle[k][0:3] for k in range(0, 3)]
                            elif col < 6:
                                square = [puzzle[k][3:6] for k in range(0, 3)]
                            else:
                                square = [puzzle[k][6:9] for k in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [puzzle[k][0:3] for k in range(3, 6)]
                            elif col < 6:
                                square = [puzzle[k][3:6] for k in range(3, 6)]
                            else:
                                square = [puzzle[k][6:9] for k in range(3, 6)]
                        else:
                            if col < 3:
                                square = [puzzle[k][0:3] for k in range(6, 9)]
                            elif col < 6:
                                square = [puzzle[k][3:6] for k in range(6, 9)]
                            else:
                                square = [puzzle[k][6:9] for k in range(6, 9)]
                        if not (number in (square[0:2])):
                            puzzle[row][col] = number
                            if checkPuzzleComplete(puzzle):
                                return True
                            else:
                                if makePuzzle(puzzle):
                                    return True
            break
    puzzle[row][col] = 0



def solvePuzzle(puzzle):
    global solutionsFound
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if puzzle[row][col] == 0:
            for number in range(1,10):
                if not(number in puzzle[row]):
                    if not(number in (
                    puzzle[0][col], puzzle[1][col], puzzle[2][col], puzzle[3][col], puzzle[4][col], puzzle[5][col], puzzle[6][col],
                    puzzle[7][col], puzzle[8][col])):
                        if row < 3:
                            if col < 3:
                                square = [puzzle[k][0:3] for k in range(0, 3)]
                            elif col < 6:
                                square = [puzzle[k][3:6] for k in range(0, 3)]
                            else:
                                square = [puzzle[k][6:9] for k in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [puzzle[k][0:3] for k in range(3, 6)]
                            elif col < 6:
                                square = [puzzle[k][3:6] for k in range(3, 6)]
                            else:
                                square = [puzzle[k][6:9] for k in range(3, 6)]
                        else:
                            if col < 3:
                                square = [puzzle[k][0:3] for k in range(6, 9)]
                            elif col < 6:
                                square = [puzzle[k][3:6] for k in range(6, 9)]
                            else:
                                square = [puzzle[k][6:9] for k in range(6, 9)]
                        if not(number in square[0:2]):
                            puzzle[row][col] = number
                            if checkPuzzleComplete(puzzle):
                                solutionsFound += 1
                                break
                            else:
                                if solvePuzzle(puzzle):
                                    return True
            break
    puzzle[row][col] = 0




makePuzzle(puzzle)
drawPuzzle(puzzle)
pygame.display.update()

solutionsFound = 0
misses = 10
#fullPuzzle = puzzle.copy()
while misses > 0:
    row = randint(0, 8)
    col = randint(0, 8)
    while puzzle[row][col] == 0:
        row = randint(0, 8)
        col = randint(0, 8)
    backup = puzzle[row][col]
    puzzle[row][col] = 0
    testPuzzle = puzzle.copy()
    solutionsFound = 0
    solvePuzzle(testPuzzle)
    if solutionsFound != 1:
        puzzle[row][col] = backup
        misses -= 1
    #misses -=1

numZero = 0
for row in range(0, 9):
    for col in range(0, 9):
        if puzzle[row][col] == 0:
            numZero += 1
print("There are {} empty spaces in your Sudoku!".format(numZero))
screen.fill((255,255,255))
drawPuzzle(puzzle)
pygame.display.update()

active = False
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for box in blankSpaces:
            box.handle_event(event)

    #for box in blankSpaces:
     #   box.update

    for box in blankSpaces:
        box.draw(screen)

    pygame.display.flip()


