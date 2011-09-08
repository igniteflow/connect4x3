

ROWS = 6
COLUMNS = 7

def print_board(board):
    for row in zip(*board):
        for column in row:
            print (column if column else '.'),
        print

    for column in range(7):
        print column+1,
    print

def win_state(board):
    return False

def insert(board, column, player):
    return

def ai_move(board, current_player):
    return

def take_input(board):
    col = raw_input()

    while True:
        try:
            col = int(col)
        except ValueError:
            continue
        else:
            return col


def main():
    board = [[None for x in range(ROWS)] for y in range(COLUMNS)]

    current_player = 'X'
    other_player = 'O'

    ai = None
    
    while True:
        if ai == current_player:
            ai_move(board, current_player)
        else:
            print_board(board)
            col = take_input(board)
            insert(board, col, current_player)

        if win_state(board):
            print 'Winner!'
            return

if __name__ == '__main__':
    main()
