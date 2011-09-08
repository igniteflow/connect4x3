import unittest

COLS = 7
ROWS = 6

verticals = [[(i, j), (i, j+1), (i, j+2), (i, j+3)] for i in range(COLS) for j in range(ROWS-3)]

horizontals = [[(i, j), (i+1, j), (i+2, j), (i+3, j)] for i in range(COLS-3) for j in range(ROWS)]

diags1 = [[(i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3)] for i in range(COLS-3) for j in range(ROWS-3)]

diags2 = [[(i, j+5), (i+1, j+4), (i+2, j+3), (i+3, j+2)] for i in range(COLS-3) for j in range(ROWS-3)]

winning_posistions = verticals + horizontals + diags1 + diags2

def winboard(board):
    for pos in winning_posistions:
        x = ''.join([board[i][j] for j, i in pos])
        return (x == 'XXXX') or (x == 'OOOO')
            

class WinTest(unittest.TestCase):
    def test1(self):
        board = [[None for x in range(ROWS)] for y in range(COLS)]
        for i in range(4):
            board[i][0] = 'X'
        self.assert_(winboard(board))

if __name__ == "__main__":
    unittest.main()

        
