from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def display_gesture_options(self):
        print("")

    def human_input(self):
        self.chosen_gesture = input("Enter gesture")