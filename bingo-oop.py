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
        elif answer < self.__rand_num:
            return ("Choose higher number")
        elif answer == self.__rand_num:
            return ("Bingo %s You did it" % self.name)
        self.__win_state = True
        self.__minus_guess_left()

    def __minus_guess_left(self):
        self.__guess_left -= 1

    def has_guess_left(self):
        if self.__guess_left > 0:
            return True
        return False

    def has_won(self):
        return self.__win_state
    
    @classmethod
    def game_has_winner(cls)
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False