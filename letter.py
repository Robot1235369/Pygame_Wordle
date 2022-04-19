import pygame
from vars import *
pygame.init()

class letter:
    def __init__(self, character, box):
        self.character = character
        self.char = font.render(self.character, False, WHITE)
        self.rect = self.char.get_rect()
        self.rect.center = (box.x + (box_size // 2), box.y + (box_size // 2))
    
    def draw(self):
        board.blit(self.char, self.rect)