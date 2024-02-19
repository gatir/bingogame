import random


class BingoGame:
    player_list = []

    def __init__(self):
        self.name = input("Enter your name: ")
        self.__rand_num = random.randint(0, 10)
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)

    def check_answer(self):
        answer = int(input(f"\n{self.name} Enter your guess: "))
        if answer > self.__rand_num:
            print("choose lower number")
        elif answer < self.__rand_num:
            print("Choose higher number")
        elif answer == self.__rand_num:
            print("Bingo %s You did it" % self.name)
            self.__win_state = True
        self.__minus_guess_left()

    def __minus_guess_left(self):
        self.__guess_left -= 1
        print(f"{self.__guess_left} guesses left")

    def has_guess_left(self):
        if self.__guess_left > 0:
            return True
        return False

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winner(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False


class GameController():
    def __init__(self):
        while True:
            for player in BingoGame.player_list:
                if not player.has_won():
                    player.check_answer()
            if BingoGame.game_has_winner():
                break


# if __name__ == "__main__":
while True:
    order = input("What you want to do? \norder: ")
    if order == "add":
        BingoGame()
    elif order == "start":
        GameController()
    elif order == "reset":
        BingoGame.player_list = []
        BingoGame()
    elif order == "exit":
        break
