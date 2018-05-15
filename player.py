#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#  

from ps10pr1 import Board


class Player:
    
    def __init__(self, checker):
        """ initializing the following two attributes
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        
        self.num_moves = 0
  
    def __repr__(self):
        """returns a string representing a Player object
        """
        return "Player " + str(self.checker)

    def opponent_checker(self):
        """ returns a one-character string representing the checker
        of the Player object’s opponent
        """
        if self.checker=='O':
            return 'X'
        else:
            return 'O'
        
    def next_move(self, board):
        """accepts a Board object as a parameter and returns the column
        where the player wants to make the next move
        """
        col=int(input('Enter a column:'))
        
        while board.can_add_to(col)==False:
            print('Try again!')
            col=int(input('Enter a column:'))
        self.num_moves+=1            
        return col
        
        
