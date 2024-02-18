# bingo game functional
import random
randnum = random.randint(0, 10)
guess_left = 3
user_name = input('Enter your name: ')


def check_answer(answer):
    if answer > randnum:
        return (False, "choose lower number")
    if answer < randnum:
        return (False, "Choose higher number")
    if answer == randnum:
        return (True, "Bingo %s You did it" % user_name)


while True:
    if guess_left == 0:
        print(user_name, " you ran out of guess..losser")
        break
    answer_input = int(input("enter your guess: "))
    answer_result = check_answer(answer_input)
    if answer_result[0] == False:
        print(answer_result[1])
    else:
        print(answer_result[1])
        break
    guess_left -= 1
