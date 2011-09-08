import random

class Opponent():

    def __init__(self, color, ROWS):
        """initiate a random"""
        self.color = color
        self.ROWS = ROWS

    def opponent_next_step_rand(self, board):
        """Returns an int between 0 - ROWS"""
        return random.randint(0, self.ROWS)

    def move(self, board):
        dumb_ai_move = self.check_columns(board)
        if dumb_ai_move is not None:
             return dumb_ai_move

        return self.opponent_next_step_rand(board)

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
  	        
        

if __name__ == "__main__":
    o = Opponent('X', 6)
    board = [['X' * 6], ['', '', '', '', 'X', 'X']]
    print o.move(board)
    print
    print
    print
    print
    board = [['', '', '', '', 'X', 'X'], ['X' * 6]]
    print o.move(board)

