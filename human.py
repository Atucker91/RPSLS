from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def display_gesture_options(self):
        print("You can choose : Rock, Paper, Scissors, Lizard, Spock")

    def human_input(self):
        self.chosen_gesture = input("Enter your chose gesture: ")
        while (
            self.chosen_gesture.lower() != "rock"
            or self.chosen_gesture.lower() != "paper"
            or self.chosen_gesture.lower() != "scissor"
            or self.chosen_gesture.lower() != "lizard"
            or self.chosen_gesture.lower() != "spock"
        ):
            self.chosen_gesture = input(
                "!!Invalid selection!!Enter your chose gesture: "
            )
