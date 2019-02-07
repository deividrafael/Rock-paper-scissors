import random

moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):

        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move):
        self.my_move = my_move


class HumanPlayer(Player):
    def move(self):
        humnan_move = input('rock, paper or scissors\n')
        while True:
            if humnan_move == 'rock':
                return humnan_move
                break
            elif humnan_move == 'paper':
                return humnan_move
                break
            elif humnan_move == 'scissors':
                return humnan_move
                break
            else:
                print('Type again!')
                humnan_move = input('rock, paper or scissors\n')
        return humnan_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflctPlayer(Player):
    def __init__(self):

        super().__init__()
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.my_move


class CyclePlayer(Player):
    def __init__(self):

        super().__init__()
        self.their_move = 0

    def move(self):
        move = None
        if self.their_move == 0:
            move = random.choice(moves)
            self.their_move += 1
        elif self.their_move == 1:
            move = 'paper'
            self.their_move += 1
        else:
            move = 'scissors'
            self.their_move += 1
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.winp1 = 0
        self.winp2 = 0

    def placar(self):
        self.score = 0
        return self

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1} \nOpponent played {move2}")
        self.placar(move1, move2)

        self.p1.learn(move2)
        self.p2.learn(move1)

    def placar(self, move1, move2):

        if move1 == move2:
            print('Empate!!!')
        elif beats(move1, move2):
            self.p1.score += 1
        else:
            self.p2.score += 1

        print(f'Score: Player one {self.p1.score}, player two {self.p2.score}')

    def anuncio(self):
        if self.p1.score > self.p2.score:
            print('*'*22 + 'Player one win!' + '*'*22)
            print(f'Player two {self.p1.score}!!')
            print(f'Player two {self.p2.score}!!')
        elif self.p2.score > self.p1.score:
            print('*'*22 + 'Player two win!'+'*'*22)
            print(f'Player two {self.p2.score}!!')
            print(f'Player two {self.p1.score}!!')
        else:
            print('*' * 22 + 'Temos um empate!' + '*' * 22)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print('-='*30)
        self.anuncio()
        print("Game over!")

    def jogo_unico(self):
        print("Game start!")
        print("Round 1 de 1:")
        self.play_round()
        self.anuncio()
        print("Game Over!")


def quebra_de_linha(string):
    return'\n'.join(string)


if __name__ == '__main__':

    while True:
        titulo = ['Escolha seu oponente digitando:',
                  '[1]Player', '[2]RandomPlayer',
                  '[3]ReflctPlayer', '[4]CyclePlayer', '']

        opponent = input(quebra_de_linha(titulo))
        if opponent == '1':
            opponent = Player()
            break
        elif opponent == '2':
            opponent = RandomPlayer()
            break
        elif opponent == '3':
            opponent = ReflctPlayer()
            break
        elif opponent == '4':
            opponent = CyclePlayer()
            break
        else:
            print('Type again!')
            opponent = input(quebra_de_linha(titulo))

    game = Game(HumanPlayer(), opponent)
    while True:
        titulo_round = ['Quantas rodadas voce deseja jogar:',
                        'Para um round digite[1]',
                        'Para mais rounds digite[2]', '']

        games = input(quebra_de_linha(titulo_round))
        if games == '1':
            game.jogo_unico()
            break
        elif games == '2':
            game.play_game()
            break
        else:
            print('Type again!')
            games = input(quebra_de_linha(titulo_round))
