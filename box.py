import pygame
from vars import *

class box:

    def __init__(self, x, y):
        global box_size
        self.x = x
        self.y = y
        self.color = None
        self.rectangle = pygame.Rect(x, y, box_size, box_size)
    
    def draw(self, surface):
        global BOX_COLOR
        global GREEN
        global YELLOW
        global GREY
        if self.color == None:
            pygame.draw.rect(surface, BOX_COLOR, self.rectangle, 3)
        elif self.color == "green":
            pygame.draw.rect(surface, GREEN, self.rectangle)
        elif self.color == "yellow":
            pygame.draw.rect(surface, YELLOW, self.rectangle)
        elif self.color == "grey":
            pygame.draw.rect(surface, GREY, self.rectangle)

    def change_color(self, new_color):
        self.color = new_color