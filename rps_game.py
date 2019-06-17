#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""
p_one_score = 0
p_two_score = 0


class Player:
    my_move = None
    their_move = None

    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):

    def move(self):
        while True:
            my_move = input("Enter rock, paper, or scissors: ")
            if my_move.lower() not in moves:
                print('Invaild Input, Try Again.\n'
                      'Enter rock, paper, or scissors\n')
            else:
                return my_move.lower()

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):

    def move(self):
        if self.their_move == 'scissors':
            return 'scissors'
        elif self.their_move == 'paper':
            return 'paper'
        else:
            return 'rock'


class CyclePlayer(Player):

    def move(self):
        if self.my_move is 'rock':
            return 'paper'
        elif self.my_move is 'paper':
            return 'scissors'
        else:
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2) is True:
            print('Player 1 Wins')
            self.p1.score += 1
        elif beats(move2, move1) is True:
            print('Player 2 Wins')
            self.p2.score += 1
        else:
            print('TIE')

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(f"SCORE - Player One: {self.p1.score}\n"
                  f"Player Two: {self.p2.score} \n")
        if self.p1.score > self.p2.score:
            print('Player One Wins!')
        elif self.p2.score > self.p1.score:
            print('Player Two Wins!')
        else:
            print('The game ended in a TIE')
        print("Game over!")

    def play_single(self):
        print("Game start!")
        print(f"Round 1 of 1:")
        self.play_round()
        print(f"SCORE - Player One: {self.p1.score}\n"
              f"Player Two: {self.p2.score} \n")
        if self.p1.score > self.p2.score:
            print('Player One Wins!')
        elif self.p2.score > self.p1.score:
            print('Player Two Wins!')
        else:
            print('The game ended in a TIE')
            print("Game over!")


if __name__ == '__main__':
    round = input('Enter \'single\' or \'full\' game: ')
    game = Game(HumanPlayer(), RandomPlayer())
    if round == 'single':
        game.play_single()
    elif round == 'full':
        game.play_game()
    else:
        print('Invalid Entry, try again.')
        round = input('Enter \'single\' or \'full\' game: ')
