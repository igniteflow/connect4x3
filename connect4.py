

def print_board(board):
    for row in board:
        for column in row:
            print column,
        print

def win_state(board):
    return False

def main():
    board = [[None for x in range(6)] for y in range(7)]
    
    while True:
        data = raw_input()
        print_board(board)
        if win_state(board):
            print 'Winner!'
            return

if __name__ == '__main__':
    main()
