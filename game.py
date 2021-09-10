from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]

    def welcome_message(self):
        pass
        # display rules
        # choose player v player or player v ai
        # display amount of rounds (3)

    def determine_game_type(self):
        pass
        # if statement on what type of players are in game
        # calls out to 

    def compare_gestures(self):
        pass

    def pvp_game(self):
        human_player1 = Human()
        human_player1.name = input("Enter player one name ")
        human_player2 = Human()
        human_player2.name = input("Enter player two name ")

    def pvai_game(self):
        
        human_player1 = Human()
        human_player1.name = input("Enter player name ")
        ai_player2 = AI()
        ai_player2.name = "Sheldon"
        



        