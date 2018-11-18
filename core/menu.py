from .titleVisualizer import TitleVisualizer
from .command import command as cmd
import collections
import os


class Menu:
    def __init__(self, gameData):
        self.data = gameData
        pass

    def enter(self):
        self.clearScreen()
        print(TitleVisualizer("Menu"))

        actions = {
            "1": cmd.NewGameCommand("New Game", self.data),
            "2": cmd.HighscoreBoardCommand("Highscores"),
            "3": cmd.HelpCommand("Help"),
            "q": cmd.QuitCommand("Quit Game", self.data)
        }

        orderedActions = collections.OrderedDict(sorted(actions.items()))

        actionPrompts = "\n"
        for key, value in orderedActions.items():
            actionPrompts += ("\t{} - {}\n".format(key, value.title))

        print(actionPrompts)
        choice = input("Input=> ")

        if choice in actions:
            actions[choice].execute()

    def clearScreen(self):
        os.system('cls')
