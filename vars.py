import pygame
from random import randint
pygame.init()

with open ('words/answers.txt', 'r') as a:
    answers = a.read().split()

with open ('words/guesses.txt', 'r') as g:
    guesses = g.read().split()

WIDTH, HEIGHT = 800, 900
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("WORDLE")
board = pygame.Surface((570, 810))
running = True
FPS = 60

# colors
BACKGROUND = (15, 15, 15)
WHITE = (255, 255, 255)
BOX_COLOR = (150, 150, 150)
GREEN = (50, 205, 50)
YELLOW = (255, 215, 0)
GREY = (128, 128, 128)

title_font = pygame.font.Font('freesansbold.ttf', 50)
font = pygame.font.Font('freesansbold.ttf', 60)
buttons = {pygame.K_a: "A", pygame.K_b: "B", pygame.K_c: "C", pygame.K_d: "D", pygame.K_e: "E", pygame.K_f: "F", pygame.K_g: "G", pygame.K_h: "H", pygame.K_i: "I", pygame.K_j: "J", pygame.K_k: "K", pygame.K_l: "L", pygame.K_m: "M", pygame.K_n: "N", pygame.K_o: "O", pygame.K_p: "P", pygame.K_q: "Q", pygame.K_r: "R", pygame.K_s: "S", pygame.K_t: "T", pygame.K_u: "U", pygame.K_v: "V", pygame.K_w: "W", pygame.K_x: "X", pygame.K_y: "Y", pygame.K_z: "Z"}

title = title_font.render('WORDLE', False, WHITE)
title_rect = title.get_rect()
title_rect.center = (board.get_size()[0] // 2, 50)
boxes = []
box_size = 100
between = 15
for i in range(6):
    boxes.append([])

# game
answer = randint(0, len(answers) + 1)
answer = answers[answer]
guess_num = 0
guess = ""
word = answers[randint(0, len(answers) - 1)]
letters = [[], [], [], [], [], []]
win = False