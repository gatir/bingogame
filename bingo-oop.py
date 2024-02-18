import random


class BingoGame:
    player_list = []

    def __init__(self):
        self.name = input("Enter your name: ")
        self.__rand_num = random.randint(0, 10)
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)

    def check_answer(self, answer):
        if answer > self.__rand_num:
            return ("choose lower number")
        if answer < self.__rand_num:
            return ("Choose higher number")
        if answer == self.__rand_num:
            return ("Bingo %s You did it" % self.name)

    def __minus_guess_left(self):
        self.__guess_left -= 1
