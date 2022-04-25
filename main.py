import pygame
from vars import *
from keys import *
from game_board import *
from sys import exit
pygame.init()

def update():
    global win
    display.fill(BACKGROUND)
    draw_board()
    pygame.display.update()
    if win == True:
        print("you won")
        exit()

def main():
    global running
    clock = pygame.time.Clock()
    create_board()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            type(event)
            
        update()

    pygame.quit()

if __name__ == '__main__':
    main()