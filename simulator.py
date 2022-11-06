
from datetime import date

from chess import Board, pgn

from engines.base_engine import Engine


class Simulator():
    def __init__(self, e1, e2):
        self.board = Board()
        self.results = []
        self._e1 = e1
        self._e2 = e2

    @property
    def pgn(self):
        game = pgn.Game()
        game.setup(Board())
        node = game

        for move in self.board.move_stack:
            node = node.add_main_variation(move)

        # Set PGN headers
        del game.headers["Site"]
        del game.headers["Round"]
        game.headers["Event"] = "Engine Challange"
        game.headers["White"] = repr(self._e1)
        game.headers["Black"] = repr(self._e2)
        game.headers['Result'] = getattr(
            self.board.outcome(), "result", lambda: "?")()
        game.headers['Date'] = date.today().strftime("%Y.%m.%d")

        return str(game)

    def play(self, e1_white=True):
        self.board.reset()

        # Determine side for each engine
        e_white = self._e1 if e1_white else self._e2
        e_black = self._e2 if e1_white else self._e1

        while self.board.outcome() is None:
            move = (e_white if self.board.turn else e_black).get_move(self.board)
            self.board.push(move)

        return self.board.outcome()

    def match(self, iterations_per_side=100, save_pgn=False):
        self.results = []

        for e1_white in [True, False]:
            for i in range(iterations_per_side):
                outcome = self.play(e1_white)

                if outcome.winner is None:
                    e1_score = .5
                else:
                    winner = outcome.winner
                    e1_score = int(winner) if e1_white else int(not winner)

                result = {
                    "i": i,
                    "e1_white": e1_white,
                    "e1": e1_score,
                    "e2": 1 - e1_score,
                }

                if save_pgn:
                    result["pgn"] = self.pgn

                self.results.append(result)

        return self.results
