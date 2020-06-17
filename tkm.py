
import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player):
    def __init__(self):
        self.previous_move2 = random.choice(moves)

    def move(self):
        return self.previous_move2

    def learn(self, my_move, their_move):
        self.previous_move2 = their_move

class CyclePlayer(Player):
    def __init__(self):
        self.previous_move1 = random.choice(moves)

    def move(self):
        moves_available = moves.index(self.previous_move1)
        if moves_available == 2:
            return moves[0]
        else:
            return moves[moves_available + 1]

    def learn(self, my_move, their_move):
        self.previous_move1 = my_move

class Human(Player):
    def move(self):
        your_move = ""
        while True:
            your_move = input('Your move: (rock / paper / scissors)\n')
            if your_move.lower() == 'r' or your_move.lower() == 'rock':
                your_move = 'rock'
                break
            elif your_move.lower() == 'p' or your_move.lower() == 'paper':
                your_move = 'paper'
                break
            elif your_move.lower() == 's' or your_move.lower() == 'scissors':
                your_move = 'scissors'
                break
            else:
                print("Invalid input, try again!")
        return your_move

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_one = 0
        self.player_two = 0
        self.tiegame = 0
        self.rounds_played = 0

    def game_header(self):
        print(
            "\n"
            "--------------------------\n"
            "Rock, Paper, Scissors\n"
            "--------------------------\n"
            "Rules:\n"
            " Scissors cuts Paper\n"
            " Paper covers Rock\n"
            " Rock crushes Scissors\n"
            "--------------------------\n")

    def select_mode(self):
        while True:
            rounds_num = input("number of rounds you would "
                               "like to play (1-10): ")
            if rounds_num.isnumeric():
                rounds_num = int(rounds_num)
                if rounds_num >= 0 and rounds_num <= 10:
                    print("-----------------------------")
                    print(f"Awesome! Let's play {rounds_num} rounds!")
                    print("-----------------------------")
                    self.rounds_played = rounds_num
                    break
                else:
                    print("That's not a number between 1 to 10, try again.")

    def select_oppenent(self):
        print(
            "Select your opponent:\n"
            "\n[B]asic  - 'rock' is played by opponent every round"
            "\n[R]andom - opponent plays random choice"
            "\nRe[F]lect - opponent mimics your move next round"
            "\n[C]ycle  - remembers what was played and cycles through moves"
            "\n[Q]uit   - quits the game"
            "\n ")
        while True:
            opponent = (input("Choose your opponent: "))
            if opponent.lower() == "b" or opponent.lower() == "basic":
                self.p2 = Player()
                break
            elif opponent.lower() == "r" or opponent.lower() == "random":
                self.p2 = RandomPlayer()
                break
            elif opponent.lower() == "f" or opponent.lower() == "reflect":
                self.p2 = ReflectPlayer()
                break
            elif opponent.lower() == "c" or opponent.lower() == "cycle":
                self.p2 = CyclePlayer()
                break
            elif opponent.lower() == "q" or opponent.lower() == "quit":
                print("You have chosen to leave the game :(")
                self.rounds_played = 0
                break
            else:
                print("That's not one of the options, try again.")

    def outcome(self, first_play, second_play):
        if beats(first_play, second_play):
            self.player_one += 1
            print(f"move '{first_play}' beats '{second_play}'. First Player won round!")
            print("Score:")
            print(f"First player: {self.player_one}")
            print(f"Second player: {self.player_two}")
            print(f"Ties: {self.tiegame}")
        elif beats(second_play, first_play):
            self.player_two += 1
            print(f"move {second_play} beats {first_play}. Second Player won round!")
            print("Score:")
            print(f"First player: {self.player_one}")
            print(f"Second player: {self.player_two}")
            print("Ties: {self.tiegame}")
        else:
            self.tiegame += 1
            print("Nobody won, it's a tie")
            print("Score:")
            print(f"First player: {self.player_one}")
            print(f"Second player: {self.player_two}")
            print(f"Ties: {self.tiegame}")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.outcome(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def fight(self):
        if self.rounds_played >= 1:
            print("\n----------------------------------")
            print("Prepare to FIGHT")
            for round in range(0, self.rounds_played):
                print("----------------------------------\n")
                print("Round {" + str(round + 1) + "}: ")
                self.play_round()

    def game_results(self):
        # Results of the game
        if self.rounds_played >= 1:
            print("\n----------------------------------")
            print("Overall score:")
            print(f"Player One won: {self.player_one}")
            print(f"Player Two won: {self.player_two}")
            print(f"Ties: {self.tiegame}")
            print("----------------------------------")
            if self.player_one > self.player_two:
                print("Player One won!")
            elif self.player_one < self.player_two:
                print("Player Two won!")
            else:
                print("It's a tie!")

            print("Thank you for playing.")
            print("----------------------------------")

    def play_game(self):
        self.game_header()
        self.select_mode()
        self.select_oppenent()
        self.fight()
        self.game_results()

if __name__ == '__main__':
    game = Game(Human(), RandomPlayer())
    game.play_game()
