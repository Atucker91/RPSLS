from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.game_type = ""
        self.game_rounds = 3
        self.rounds_to_win = 2

    def welcome_message(self):
        print(
            "Are you ready for the intensity of RPSLS?  You pick a gesture from the provided list and hope that you pick better than your opponent!! The win conditions are as follows: \nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n"
        )
        self.determine_game_type()

    def determine_game_type(self):
        user_input = input(
            "Choose whether you would like to defeat a friend: Player VS Player (PVP) or whether you would like to play against the computer: Player VS AI (PVAI) game:  "
        )
        if user_input.upper() == "PVP":
            self.game_type = "PVP"
            self.pvp_game_setup()
        elif user_input.upper() == "PVAI":
            self.game_type = "PVAI"
            self.pvai_game_setup()
        else:
            print('Please enter either "PVP" or "PVAI"')
            self.determine_game_type()

    def pvp_game_setup(self):
        human_player1 = Human()
        human_player1.name = input("\nEnter player one name ")
        human_player2 = Human()
        human_player2.name = input("\nEnter player two name ")
        self.determine_game_rounds()
        self.pvp_game(human_player1, human_player2)

    def pvai_game_setup(self):
        human_player1 = Human()
        human_player1.name = input("Enter player name ")
        ai_player2 = AI()
        ai_player2.name = "Sheldon"
        self.determine_game_rounds()
        self.pvai_game(human_player1, ai_player2)

    def pvp_game(self, human_player1, human_player2):
        print(
            f"\n{human_player1.name}, please select your gesture with which to defeat {human_player2.name}.  Make sure they close their eyes before you pick!"
        )
        human_player1.display_gesture_options()
        human_player1.human_input()
        print(f"\n{human_player2.name}, what gesture do you retaliate with?")
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
        if player1.chosen_gesture.lower() == player2.chosen_gesture:
            pass
        elif player1.chosen_gesture.lower() == "rock":
            self.compare_rock(player1, player2)
        elif player1.chosen_gesture.lower() == "paper":
            self.compare_paper(player1, player2)
        elif player1.chosen_gesture.lower() == "scissors":
            self.compare_scissors(player1, player2)
        elif player1.chosen_gesture.lower() == "lizard":
            self.compare_lizard(player1, player2)
        elif player1.chosen_gesture.lower() == "spock":
            self.compare_spock(player1, player2)

        print(
            f"\nAfter round score is now: \n {player1.name}:{player1.rounds_won}, {player2.name}:{player2.rounds_won}"
        )

        if (
            player1.rounds_won == self.rounds_to_win
            or player2.rounds_won == self.rounds_to_win
        ):
            if player1.rounds_won == self.rounds_to_win:
                print(f"\n{player1.name}, YOU HAVE DEFEATED YOUR OPPONENT!!")
                self.play_again(player1, player2)
            elif player2.rounds_won == self.rounds_to_win:
                print(f"\n{player2.name}, YOU KICKED BUTT!! VICTORY!!")
                self.play_again(player1, player2)

        else:
            if self.game_type == "PVP":
                self.pvp_game(player1, player2)
            elif self.game_type == "PVAI":
                self.pvai_game(player1, player2)

    def compare_rock(self, player1, player2):
        if (
            player2.chosen_gesture.lower() == "scissors"
            or player2.chosen_gesture.lower() == "lizard"
        ):
            player1.rounds_won += 1
        else:
            player2.rounds_won += 1

    def compare_paper(self, player1, player2):
        if (
            player2.chosen_gesture.lower() == "rock"
            or player2.chosen_gesture.lower() == "spock"
        ):
            player1.rounds_won += 1
        else:
            player2.rounds_won += 1

    def compare_scissors(self, player1, player2):
        if (
            player2.chosen_gesture.lower() == "paper"
            or player2.chosen_gesture.lower() == "lizard"
        ):
            player1.rounds_won += 1
        else:
            player2.rounds_won += 1

    def compare_lizard(self, player1, player2):
        if (
            player2.chosen_gesture.lower() == "spock"
            or player2.chosen_gesture.lower() == "paper"
        ):
            player1.rounds_won += 1
        else:
            player2.rounds_won += 1

    def compare_spock(self, player1, player2):
        if (
            player2.chosen_gesture.lower() == "scissors"
            or player2.chosen_gesture.lower() == "rock"
        ):
            player1.rounds_won += 1
        else:
            player2.rounds_won += 1

    def reset_game(self, player1, player2):
        player1.rounds_won = 0
        player2.rounds_won = 0
        self.determine_game_type()

    def play_again(self, player1, player2):
        y_or_no = input("Play again? Enter yes or no ")
        if y_or_no.lower() == "yes":
            self.reset_game(player1, player2)
        elif y_or_no.lower() == "no":
            print(
                "\nWe hope you enjoyed this epic game of RPSLS.  Consider playing again in the future!"
            )
        else:
            print('Please enter "yes" or "no"')
            self.play_again(player1, player2)

    def determine_game_rounds(self):
        self.game_rounds = int(
            input(
                "Please enter how many rounds of RPSLS you would like to play.  Remember, it has to be an odd number so that someone can win!"
            )
        )
        if self.game_rounds % 2 == 1:
            self.rounds_to_win = (self.game_rounds + 1) / 2
        else:
            print("Please input an odd number!")
            self.determine_game_rounds()
