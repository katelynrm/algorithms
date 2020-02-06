import random


BEATS = [('R', 'S'), ('S', 'P'), ('P', 'R')]
# play the thing that didn't come up - rock beats scissors = play paper

# if you win - loser expects same play so if you just won with rock, play what they just played - scissors


# if computer wins - play what they just played
# if computer loses = play what would have beaten the previous - play that didn't come up C: paper H: scissors - next play Rock


class RPS:
    def __init__(self):
        self.human_previous_play = ""  # caching
        self.computer_previous_play = ""
        self.last_round_winner = ""
        self.human_score = 0
        self.computer_score = 0
        self.round = 0

    def play(self):

        if self.round == 0:
            play = random.choice(["R", "P", "S"])
            play = 'R'
            self.computer_previous_play = play
            return play

        elif self.last_round_winner == 'D':
            play = random.choice(["R", "P", "S"])
            self.computer_previous_play = play
            return play

        elif self.last_round_winner == "C":
            # print('elif for C')
            return self.next_play_if_won()

        elif self.last_round_winner == "H":
            # print('elif for H')
            return self.next_play_if_lost()
        else:
            print('went wrong')
        

    def next_play_if_lost(self):
        for tup in BEATS:
            if tup[1] == self.human_previous_play:
                self.computer_previous_play = tup[0]
                return tup[0]

    def next_play_if_won(self):
        self.computer_previous_play = self.human_previous_play
        return self.computer_previous_play

    def who_won_round(self, human_play):
        self.round += 1
        self.human_previous_play = human_play.upper()
        C = self.computer_previous_play
        H = self.human_previous_play
        if C == H:
            print('draw')
            self.last_round_winner = "D"
        elif human_play not in ["R","P","S"]:
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



if __name__ == "__main__":
    game = RPS()
    print('Type the following letters for plays: \n R: rock \n S: scissors \n P: paper')
    while game.human_score < 2 and game.computer_score < 2:
        human_play = input("Type your play human: ")
        computer_play = game.play()
        print("Computer's play:", computer_play)
        game.who_won_round(human_play)

    if game.human_score > game.computer_score:
        print("Human won the game!")
        print(game.human_score, game.computer_score)
    else:
        print('Computer won the game!')
        print(game.human_score, game.computer_score)
