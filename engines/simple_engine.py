import chess
from chess import Move


class SimpleEngine:

    PIECE_VALUE = {
        None: 0,
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3.01,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 90
    }

    def __repr__(self) -> str:
        return 'AlmostAlpha0'

    def get_move(self, board):
        best_move, value = Move.null, float("-inf")

        for move in board.legal_moves:
            captured_piece = board.piece_at(move.to_square)

            new_value = 0 if captured_piece is None else self.PIECE_VALUE[captured_piece.piece_type]

            if new_value > value:
                best_move, value = move, new_value

        return best_move
