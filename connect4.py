#!/usr/bin/python
import opponent
import time

ROWS = 6
COLUMNS = 7

import winner

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
    bot = opponent.Opponent(ai, ROWS)

    moves = 0
    
    while True:
        if current_player == 'X':
            moves += 1
        if ai == current_player:
            time.sleep(0.5)
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
