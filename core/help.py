from .titleVisualizer import TitleVisualizer
from .scoreRules import ScoreRules
import os


class Help:
    def __init__(self):
        self.header = TitleVisualizer("Help")

    def __repr__(self):
        os.system("cls")
        print(self.header)
        result = """
Yahtzee, a game of chance played with 5 d6 dice split into two phases.

Phase 1: Rolling
    During the rolling phase, roll or hold the dice.
    Rolling up to a maximum of 3 times before the phase ends.
    Holding dice to increase chances of score a specific scoring slot.
    Holding all the dice ends the phase.

Phase 2: Scoring
    In this phase pick a score slot in which to score your dice.
    Score slots can only be scored once during a round.

End of Game:
    The game ends when all the scoring slots are filled

Highscores:
    The score for the players current round is automatically added
    into the highscore board at the end of a roundself.
    Only the top 10 scores are shown in the board.\n"""

        result += ScoreRules().__repr__()

        return result
