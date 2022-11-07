import random


class Engine:

    def __repr__(self) -> str:
        '''Cool name of the engine.'''
        return 'BaseEngine'

    def get_move(self, board):
        return random.choice(list(board.legal_moves))
