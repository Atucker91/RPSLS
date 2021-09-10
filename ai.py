from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()

    def ai_input(self):
        i = random.randint(0, 4)
        # fill in with i for ai choice
