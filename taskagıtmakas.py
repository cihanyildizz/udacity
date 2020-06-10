#!/usr/bin/env python3

import random

class Player:
    moves = ['taş', 'kağıt', 'makas']

    def __init__(self):
        self.my_move = self.moves
        self.pc_move = random.choice(self.moves)
        self.score = 0

    def learn(self, my_move, pc_move):
        self.my_move = my_move
        self.pc_move = pc_move

    def learn_past(pc_move):
        pass

    def move(self):
        return self.moves[0]

class RandomPlayer(Player):
    def move(self):
        index = random.randint(0, 2)
        return self.moves[index]

class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.pc_move = None

    def move(self):
        if self.pc_move is None:
            return Player.move(self)
        return self.pc_move

    def learn_past(self, pc_move):
        self.pc_move = pc_move

class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def move(self):
        move_human = None
        if self.last_move is None:
            move_human = Player.move(self)
        else:
            index = self.moves.index(self.last_move) + 1
            if index >= len(self.moves):
                index = 0
            move_human = self.moves[index]
        self.last_move = move_human
        return move_human

class HumanPlayer(Player):
    def move(self):
        while True:
            move_human = input('Hamleni yap (' + ', '.join(self.moves) + '):\n')
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

    def game_header(self):
        print(
            "\n"
            "--------------------------\n"
            "Taş, Kağıt, Makas\n"
            "--------------------------\n"
            "Kurallar:\n"
            " Makas kağıdı keser\n"
            " Kağıt taşı dolar\n"
            " Taş makası kırar\n"
            "--------------------------\n"
            "Şimdi yarışmaya başla !!!\n"
            ">>>> Oyu başlıyor ... <<<<"
            "\n çıkmak istersen \'çıkış\ yaz.'"
            " \n kaç round oynayacaksın soracağız))"
            )

    def beats(self, one, two):
        if (one == 'taş' and two == 'makas'):
            return True
        elif (one == 'makas' and two == 'kağıt'):
            return True
        elif (one == 'kağıt' and two == 'taş'):
            return True
        return False

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
        self.game_header()
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
