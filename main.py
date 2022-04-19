import pygame
from vars import *
from keys import *
from game_board import *
pygame.init()

def update():
    display.fill(BACKGROUND)
    draw_board()
    pygame.display.update()

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