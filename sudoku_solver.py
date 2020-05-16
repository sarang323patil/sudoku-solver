# Date - 15/MAY/2020
# Sudoku solver

import pygame
import time
from os import system, name
pygame.font.init()

board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

GAP = []  # [[row, col, number]]
WIN_HEIGHT = 630
WIN_WIDTH = 630
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

def fill_board(board, a, GAP, win):
    row = 0
    col = 0
    g = 0
    ans = False
    for i in range(0, 9):
        for j in range(0, 9):
            if(board[i][j] == 0):
                row = i
                col = j
                g = 1
                break
        if (g):
            break

    if(not g): 
        return None

    for n in range(a, 9):
        ans = check((n%9)+1, row, col, board)
        
        if(ans):
            GAP.append([row, col, (n%9)+1])
            board[row][col] = (n%9)+1
            draw(board, GAP, win)
            fill_board(board, 0, GAP, win)
            return None
    

    if(not ans and len(GAP)>0):
        rr = GAP[len(GAP)-1][0]
        cc = GAP[len(GAP)-1][1]
        board[rr][cc] = 0
        a = GAP[len(GAP)-1][2] 
        GAP.pop()
        draw(board, GAP, win)
        fill_board(board, a, GAP, win)
    else:
        return None



def check(n, row, col, board):
    for i in range(0, 9):
        if(board[row][i] == n):
            return False 

    for i in range(0, 9):
        if(board[i][col] == n):
            return False

    return True


def draw(board, GAP, win):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            return None

    win.fill((255, 255, 255))      # White back ground
    for i in range(70, 631, 70):   # Verticle Lines
        pygame.draw.line(win, (0, 0, 0), (i, 0), (i, 630), 5)
    for i in range(70, 631, 70):   # Horizontal lines
        pygame.draw.line(win, (0, 0, 0), (0, i), (630, i), 5)

    STATE_FONT = pygame.font.SysFont("arialblack", 55)
    for i in range(0, 9):
        for j in range(0, 9):
            x = i*70 + -1
            y = j*70 + 12
            if(board[i][j]):
                value = str(board[i][j])
                text = STATE_FONT.render(value, 1, (0,0,0))
                win.blit(text, (y, x))
                del text

    pygame.display.update()
    time.sleep(0.2)


draw(board, GAP, win)
fill_board(board, 0, GAP, win)

run=True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            #pygame.quit()
    draw(board, GAP, win)
    print("added interface")
