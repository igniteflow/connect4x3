

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

def main():
    board = [[None for x in range(ROWS)] for y in range(COLUMNS)]

    current_player = 'X'
    other_player = 'O'
    
    while True:
        print_board(board)

        data = raw_input()
        if win_state(board):
            print 'Winner!'
            return

if __name__ == '__main__':
    main()
