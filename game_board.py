import pygame
from vars import *
from box import box
pygame.init()

def create_board():
    for i in range(5):
        for j in range(6):
            x = (i * (box_size + between)) + 5
            y = (j * (box_size + between)) + 100
            boxes[j].append(box(x, y))

def draw_board():
    global board
    global guess_num
    global letters
    board.fill(BACKGROUND)
    board.blit(title, title_rect)
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            boxes[i][j].draw(board)
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            letters[i][j].draw()

    modifier = (display.get_size()[1] / board.get_size()[1]) * board.get_size()[0]
    new_board = pygame.transform.scale(board, (int(modifier), display.get_size()[1]))
    display.blit(new_board, ((display.get_size()[0] // 2) - (new_board.get_size()[0] // 2), 0))
