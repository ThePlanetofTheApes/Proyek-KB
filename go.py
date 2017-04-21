'''
A Go Game.
'''
from pygo1963.model.Board import InvalidMoveError, Board
from pygo1963.model.Player import AlphaBetaPlayer

from pygo1963.goLogic.GoEvaluator import AdvacedGoEvaluator
from pygo1963.model.DepthManager import DepthManager
from pygo1963.model.Constants import BLACK_COLOR, WHITE_COLOR

class Game:
    """ This class represents the Go Game."""
    
    def __init__(self, black_player, white_player, board):
        self.black_player = black_player
        self.white_player = white_player
        self.board = board
        self.next_move = BLACK_COLOR
        self._finish = False
        
    def play(self):
        
        while not self.board.game_finished and not self._finish:
            self._ask_move()

    def _ask_move(self):
        
        player = (self.black_player if self.next_move == BLACK_COLOR 
                        else self.white_player)        
        
        move = None        
        while not move:
            move = player.make_move(self.board.copy())
            
            try:
                self.board.make_move(move)            
            except InvalidMoveError:
                move = None
                player.notify_invalid_move()
        
        self.next_move = (WHITE_COLOR if self.next_move == BLACK_COLOR 
                                else BLACK_COLOR)
    
    def finish(self):
        """ Tells the game to stop asking for moves. """
        self._finish = True
        
        

if __name__ == "__main__":
    
    game = Game(AlphaBetaPlayer("white", "dx9", DepthManager(9) , AdvacedGoEvaluator(False)),
                AlphaBetaPlayer("black", "chacholano", DepthManager(9), AdvacedGoEvaluator(False)), Board(9), 0)
    game.play()