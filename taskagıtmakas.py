#!/usr/bin/env python3

import random

class Player:
    moves = ['taş', 'kağıt', 'makas']

    def __init__(self):
        self.my_move = self.moves
        self.pc_move = random.choice(self.moves)

    def learn(self, my_move, pc_move):
        self.my_move = my_move
        self.pc_move = pc_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        return self.pc_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            move_human = input("'taş', 'kağıt', 'makas'? > ")
            if move_human.lower() in self.moves:
                return move_human.lower()
            elif move_human.lower() == 'çıkış':
                exit()



class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'taş' and two == 'makas') or
                (one == 'makas' and two == 'kağıt') or
                (one == 'kağıt' and two == 'taş'))

    def rounds(self):
        while True:
            self.number_rounds = input("Kaç tur oynamak istersin? > ")
            if self.number_rounds.isdigit():
                return self.number_rounds
            elif self.number_rounds.lower() == 'çıkış':
                exit()

    def play_round(self):
        move_human = self.p1.move()
        move_pc = self.p2.move()
        if self.beats(move_human, move_pc):
            self.score_p1 += 1
            winner = '**** Kazandın Tebrikler! ****'
        elif move_human == move_pc:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = '**** Berabere ****'
        else:
            self.score_p2 += 1
            winner = '**** Bilgisayar kazandı !****'
        print(
            f"> Sen  : {move_human}"
            f"\n> bilgisayar : {move_pc}"
            f"\n{winner}"
            f"\nSonuç Sen ( {self.score_p1} ),"
            f"bilgisayar( {self.score_p2} )"
        )
        self.p1.learn(move_human, move_pc)
        self.p2.learn(move_pc, move_human)

    def play_game(self):
        print(">>>> Oyu başlıyor ... <<<<"
            "\n çıkmak istersen \'çıkış\ yaz.'"
            " \n kaç round oynayacaksın soracağız)"
        )
        self.rounds()
        for round in range(int(self.number_rounds)):
            print(f"\nRound {round + 1} --")
            self.play_round()
        if self.score_p1 == self.score_p2:
            print(
                f"\n---- Oyun berabere ----"
                f"\n sonuç: Sen ( {self.score_p1} ),"
                f"bilgisayar ( {self.score_p2} )"
            )
        elif self.score_p1 > self.score_p2:
            print(
                f"\n---- Sen kazandın ! tebrikler ----"
                f"\n sonuç: Sen ( {self.score_p1} )*,"
                f"bilgisayar ( {self.score_p2} )"
            )
        else:
            print(
                f"\n---- bilgisayar kazandı ----"
                f"\nsonuç: Sen( {self.score_p1} ),"
                f"bilgisayar  ( {self.score_p2} )*"
            )

if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
