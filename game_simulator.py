import chess
import chess.pgn

import random

class ChessGame():

    def __init__(self):
        self.board = chess.Board()
        self.current_player = 0               #0 - white, 1 - black

    def is_game_over(self):
        return any([
        self.board.is_stalemate(), 
        self.board.is_insufficient_material(),
        self.board.is_checkmate(),
        self.board.is_fivefold_repetition(),
        self.board.is_seventyfive_moves()] )

        # Optionally one could add those as game end:
        # self.board.can_claim_threefold_repetition(),
        # self.board.can_claim_fifty_moves(),
        # self.board.can_claim_draw(),

    def play_game(self):

        game_pgn = chess.pgn.Game()
        game_pgn.headers["White"] = "white"
        game_pgn.headers["Black"] = "black"
        game_pgn.setup(self.board) 

        node = game_pgn
            
        while not self.is_game_over():
            
            if not self.current_player:
                move = self.get_white_move()     
            else:
                move = self.get_black_move()

            self.board.push(move)
            node = node.add_variation(move)

            self.current_player = not self.current_player

        return self.board.outcome(), game_pgn

    def get_white_move(self):
        # INPUT HERE
        move = random.choice(list(self.board.legal_moves))
        return move

    def get_black_move(self):
        # INPUT HERE
        move = random.choice(list(self.board.legal_moves))
        return move