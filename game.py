from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        self.game_type = ""

    def welcome_message(self):
        print(
            "Best out of 3 wins!\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n"
        )
        self.determine_game_type()

    def determine_game_type(self):
        user_input = input("Choose Player VS Player (PVP) or Player VS AI (PVAI) game")
        if user_input == "PVP":
            self.game_type = "PVP"
            self.pvp_game_setup()
        elif user_input == "PVAI":
            self.game_type = "PVAI"
            self.pvai_game_setup()

    def pvp_game_setup(self):
        human_player1 = Human()
        human_player1.name = input("Enter player one name ")
        human_player2 = Human()
        human_player2.name = input("Enter player two name ")
        self.pvp_game(human_player1, human_player2)

    def pvai_game_setup(self):
        human_player1 = Human()
        human_player1.name = input("Enter player name ")
        ai_player2 = AI()
        ai_player2.name = "Sheldon"
        self.pvai_game(human_player1, ai_player2)

    def pvp_game(self, human_player1, human_player2):
        human_player1.display_gesture_options()
        human_player1.human_input()
        human_player2.display_gesture_options()
        human_player2.human_input()
        self.compare_gestures(human_player1, human_player2)

    def pvai_game(self, human_player1, ai_player2):
        human_player1.display_gesture_options()
        human_player1.human_input()
        ai_player2.ai_input()
        ai_player2.chosen_gesture = self.gestures[ai_player2.random_int]
        ai_player2.ai_display()
        self.compare_gestures(human_player1, ai_player2)

    def compare_gestures(self, player1, player2):
        if player1.chosen_gesture == player2.chosen_gesture:
           pass
        elif player1.chosen_gesture == "rock":
            if player2.chosen_gesture == "scissors" or player2.chosen_gesture == "lizard":
                player1.rounds_won +=1
            else:
                player2.rounds_won +=1
        if player1.rounds_won == 2 or player2.rounds_won == 2:
            print("YOU WIN!")
        else:
            if self.game_type == "PVP":
                self.pvp_game(player1, player2)
            elif self.game_type == "PVAI":
                self.pvai_game(player1, player2)
