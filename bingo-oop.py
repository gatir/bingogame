import random


class BingoGame:
    player_list = []

    def __init__(self):
        self.name = input("Enter your name: ")
        self.rand_num = random.randint(0, 10)
        self.guess_left = 3
        self.player_list.append(self)
