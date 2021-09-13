from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()
        self.random_int = 0

    def ai_input(self):
        self.random_int = random.randint(0, 4)

    def ai_display(self):
        print("\nThe AI chose:", self.chosen_gesture)
