# bingo game functional
import random
randnum = random.randint(0, 10)
guess_left = 4
user_name = input('Enter your name: ')


def check_answer(answer):
    if answer > randnum:
        return (False, "choose lower number")
    if answer < randnum:
        return (False, "Choose higher number")
    if answer == randnum:
        return (True, "Bingo ", user_name, "You did it")
