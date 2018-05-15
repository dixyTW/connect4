#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead=lookahead

        
    def __repr__(self):
        return "Player " + str(self.checker)+' ('+self.tiebreak +', '+str(self.lookahead)+')'
    def max_score_column(self, scores):
        maximum=max(scores)
        x=[]
        for i in range(len(scores)):
            if scores[i]==maximum:
                x+=[i]
                
        if len(x)==1:
            return x[0]
        elif self.tiebreak== 'LEFT':
            return x[0]
        elif self.tiebreak== 'RIGHT':
            return x[-1]
        else:
            return random.choice(x)
            
        
        
    def scores_for(self, board):
        """ MUST return a list of scores – one for each column!!
        """
        scores = [50] * board.width

        for col in range(board.width):
            if board.can_add_to(col)== False:
                scores[col]=-1
            elif board.is_win_for(self.checker)==True:
                scores[col]=100
            elif board.is_win_for(self.opponent_checker())==True:
                scores[col]= 0
 
            elif self.lookahead==0:
                scores[col]= 50
            else:
                board.add_checker(self.checker,col)
                opponent=AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(board)
                scores[col] = 100 - max(opp_scores)
                print("----------------This is ", self.checker, "'s score--------------------")
                print("we are on column ", col)
                print("current lookahead for ", self.checker, " is ", self.lookahead)
                print(self.opponent_checker(), "'s score is ", opp_scores)
                print(self.checker, "'s score is ", scores)
                board.remove_checker(col)
                
                
        return scores
    def next_move(self, board):
        self.scores_for(board)[-1]+1
        
"""
>>> AIPlayer('X', 'LEFT', 0).scores_for(b)
[50, 50, 50, 50, 50, 50, 50]
# A lookahead of 1 sees immediate wins.
# (O would win if it put a checker in column 3.)
>>> AIPlayer('O', 'LEFT', 1).scores_for(b)
[50, 50, 50, 100, 50, 50, 50]
# But a lookahead of 1 doesn't see possible losses!
# (X doesn't see that O can win if column 3 is left open.)
>>> AIPlayer('X', 'LEFT', 1).scores_for(b)
[50, 50, 50, 50, 50, 50, 50]
# A lookahead of 2 sees possible losses.
# (All moves by X other than column 3 leave it open to a loss.
# note that X's score for 3 is 50 instead of 100, because it
# assumes that O will follow X's move to 3 with its own move to 3,
# which will block X's possible horizontal win.)
>>> AIPlayer('X', 'LEFT', 2).scores_for(b)
[0, 0, 0, 50, 0, 0, 0]
# A lookahead of 3 sees set-up wins!
# (If X chooses column 3, O will block its horizontal win, but
# then X can get a diagonal win by choosing column 3 again!)
>>> AIPlayer('X', 'LEFT', 3).scores_for(b)
[0, 0, 0, 100, 0, 0, 0]
# With a lookahead of 3, O doesn't see the danger of not
# choosing 3 for its next move (hence the 50s in columns
# other than column 3).
>>> AIPlayer('O', 'LEFT', 3).scores_for(b)
[50, 50, 50, 100, 50, 50, 50]
# With a lookahead of 4, O **does** see the danger of not
# choosing 3 for its next move (hence the 0s in columns
# other than column 3).
>>> AIPlayer('O', 'LEFT', 4).scores_for(b)
[0, 0, 0, 100, 0, 0, 0]
"""
        
        




