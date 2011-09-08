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
	try_methods = (self.check_columns, )
	for try_method in try_methods:
	    try_move = try_method(board)
            if try_move:
                return try_move

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

#        print last_x
#        print last_o
	last_token = min(last_x, last_o)
#        print last_token
        return last_token >= 4

    def check_columns(self, board):
	for i, column in enumerate(board):
            if self.should_play_this_column(column): 
                return i
  	        
        

if __name__ == "__main__":
    o = Opponent('X', 6)
    board = [['', '', '', '', 'X', 'X'], ['X' * 6]]
    print o.move(board)

