from .state import State
from ..titleVisualizer import TitleVisualizer
from ..command import *

class MenuState(State):
    def __init__(self, title, machine, player):
        super().__init__(title, machine)
        self.player = player
        self.header = TitleVisualizer("Yahtzee Menu")

    def Enter(self):
        print(self.header)

        actions = {
            "1" : NewGameCommand("New Game", self),
            "h" : HighscoreBoardCommand("Highscores"),
            "q" : QuitCommand("Quit Game", self)
        }

        if self.player is not None:
            actions["0"] = ContinueGameCommand("Continue As " + self.player.name, self)
            actions["1"] = NewGameCommand("New Player Game", self)

        orderedActions = collections.OrderedDict(sorted(actions.items()))

        actionPrompts = "\n"
        for key, value in orderedActions.items():
            actionPrompts += ("\t{} - {}\n".format(key, value.title))

        choice = input(actionPrompts)

        if choice in actions:
            actions[choice].execute()
