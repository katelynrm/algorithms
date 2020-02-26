import random 

BEATS = [('R', 'S'), ('S', 'P'), ('P', 'R')]

class RPSgame:
    def start_game(self, level):
        if level == 'random_chance':
            RPSRandom().play_a_game()
        elif level == 'hard':
            RPSHard().play_a_game()
        else:
            raise ValueError('Must select from easy or hard')


class RPS:
    def __init__(self):
        self.human_previous_play = ""
        self.computer_previous_play = ""
        self.last_round_winner = ""
        self.human_score = 0
        self.computer_score = 0
        self.round = 0

    def play_a_game(self):
        while self.human_score < 2 and self.computer_score < 2:
            human_play = input("Human's Turn. Type your play: ")
            computer_play = self.play_a_round()
            print("Computer's Play: ", computer_play)
            self.who_won_round(human_play)
        if self.human_score > self.computer_score:
            print(f"Human won the game. \nFinal score \n Human: {self.human_score}, Computer: {self.computer_score}")
        else:
            print(f"Computer won the game. \nFinal score \n Human: {self.human_score}, Computer: {self.computer_score}")

    def who_won_round(self, human_play):
        self.round += 1
        self.human_previous_play = human_play.upper()
        C = self.computer_previous_play
        H = self.human_previous_play
        if C == H:
            print('Round winner: draw',"\n----\n")
            self.last_round_winner = "D"
        elif human_play.upper() not in ["R","P","S"]:
            raise ValueError('Must input a R, P or S') 
        else:
            for tup in BEATS:
                if (C, H) == tup:
                    self.last_round_winner = "C"
                    self.computer_score += 1
                    print("Round winner: computer","\n----\n")
                elif (H, C) == tup:
                    print("Round winner: human","\n----\n")
                    self.last_round_winner = "H"
                    self.human_score += 1

class RPSRandom(RPS):

    def __init__(self):
        super().__init__()

    def play_a_round(self):
        play = random.choice(["R", "P", "S"])
        self.computer_previous_play = play
        return play



class RPSHard(RPS):

    def __init__(self):
        super().__init__()

    def play_a_round(self):

        if self.round == 0:
            play = random.choice(["R", "P", "S"])
            self.computer_previous_play = play
            return play

        elif self.last_round_winner == 'D':
            play = random.choice(["R", "P", "S"])
            self.computer_previous_play = play
            return play

        elif self.last_round_winner == "C":
            return self.__next_play_if_won()

        elif self.last_round_winner == "H":
            return self.__next_play_if_lost()
        else:
            print('went wrong')

    def __next_play_if_lost(self):
        for tup in BEATS:
            if tup[1] == self.human_previous_play:
                self.computer_previous_play = tup[0]
                return tup[0]

    def __next_play_if_won(self):
        self.computer_previous_play = self.human_previous_play
        return self.computer_previous_play



choices = ['random_chance', 'hard']
level = 'random_chance'
level = input('would you like to play with random chance or hard?') 
game = RPSgame()
game.start_game(level)


