from connect4 import Opponent
        

if __name__ == "__main__":
    return
    o = Opponent('X', 6)
    board = [['X' * 6], ['', '', '', '', 'X', 'X']]
    print o.move(board)
    print
    print
    print
    print
    board = [['', '', '', '', 'X', 'X'], ['X' * 6]]
    print o.move(board)

