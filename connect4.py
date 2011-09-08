#!/usr/bin/python
import random
import time

ROWS = 6
COLUMNS = 7

import winner

class Opponent():

    def __init__(self, color, ROWS):
        """initiate a random"""
        self.color = color
        self.ROWS = ROWS

    def opponent_next_step_rand(self, board):
        """Returns an int between 0 - ROWS"""
        return random.randint(0, self.ROWS)

    def move(self, board):
        a_bit_smarter = self.kind_of_smart(board)
        if a_bit_smarter is not None:
             return a_bit_smarter

        dumb_ai_move = self.check_columns(board)
        if dumb_ai_move is not None:
             return dumb_ai_move

        return self.opponent_next_step_rand(board)

    def kind_of_smart(self, board):
        import copy
        for i in range(self.ROWS):
            try_board = copy.copy(board)
            insert(try_board, i, self.color)
            if win_state(try_board):
                 return i
             

    def should_play_this_column(self, column):
        try:
	    last_x = column.index('X')
        except ValueError:
	    last_x = len(column)

        try:
	    last_o = column.index('O')
        except ValueError:
	    last_o = len(column)

	last_token = min(last_x, last_o)
        return last_token >= 4

    def check_columns(self, board):
        """ loop through all the columns"""
	for i, column in enumerate(board):
            if self.should_play_this_column(column): 
                return i

def print_board(board):
    for row in zip(*board):
        for column in row:
            print (column if column else '.'),
        print

    for column in range(7):
        print column+1,
    print

def win_state(board):
    return winner.winboard(board)

def insert(board, column, player):
    for i, cell in enumerate(board[column]):
        if cell:
            board[column][i-1] = player
            return
    board[column][-1] = player
    return

def ai_move(board, current_player):
    return

def take_input(board):
    while True:
        col = raw_input()
        try:
            col = int(col.strip())
        except ValueError:
            continue
        else:
            if not 1 <= col <= COLUMNS:
                continue
            if board[col-1][0]:
                continue
            return col - 1

def main():
    board = [[None for x in range(ROWS)] for y in range(COLUMNS)]

    current_player = 'X'
    other_player = 'O'

    ai = 'X'
    bot = Opponent(ai, ROWS)

    moves = 0
    
    while True:
        if current_player == 'X':
            moves += 1
        if ai == current_player:
            time.sleep(random.random() * 3)
            col = bot.move(board)
            insert(board, col, current_player)
            print_board(board)
        else:
            col = take_input(board)
            insert(board, col, current_player)
            print_board(board)

        if win_state(board):
            print 'Winner is %s in %d moves!' % (current_player, moves)
            print_board(board)
            return

        current_player, other_player = other_player, current_player

if __name__ == '__main__':
    main()
