import pygame
from vars import *
from letter import letter
from sys import exit
pygame.init()

def leave():
    print("You lost")
    exit()

def type(event):
    global guess
    global guess_num
    global letters
    global running
    if guess_num == 6:
        leave()
    if event.type == pygame.KEYDOWN:
        for i in buttons:
            if event.key == i:
                l = buttons[i]
                if not len(guess) == 5:
                    guess = guess + l
                    letters[guess_num].append(letter(l, boxes[guess_num][len(guess) - 1]))
                    print(guess)
        if event.key == pygame.K_RETURN:
            if len(guess) == 5:
                if guess.lower() in guesses:
                    guess_num += 1
                    print(guess_num)
                    guess = ""
        if event.key == pygame.K_BACKSPACE:
            list = []
            for i in range(len(guess)):
                list.append(guess[i])
            try:
                list.pop()
                letters[guess_num].pop()
            except IndexError:
                pass
            guess = ""
            for i in range(len(list)):
                guess = guess + list[i]
            print(guess)