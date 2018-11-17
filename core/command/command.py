#! /usr/bin/python
from ..jsonSave import JsonSave
from ..player import Player
from ..highscoreBoard import HighscoreBoard
from ..help import Help


class Command:
    """Base command"""

    def __init__(self, title):
        self.title = title

    def execute(self):
        """Return command execution success"""
        return True


class SaveCommand(Command):
    def __init__(self, title, player):
        super().__init__(title)
        self.player = player

    def execute(self):
        JsonSave().save(self.player)
        return True


class QuitCommand(Command):
    def __init__(self, title, gameData):
        super().__init__(title)
        self.gameData = gameData

    def execute(self):
        self.gameData.gameEnabled = False
        self.gameData.roundEnabled = False
        return True


class EndRoundCommand(Command):
    def __init__(self, title, gameData):
        super().__init__(title)
        self.gameData = gameData

    def execute(self):
        self.gameData.roundEnabled = False
        return True


class NewGameCommand(Command):
    def __init__(self, title, gameData):
        super().__init__(title)
        self.gameData = gameData

    def execute(self):
        name = input("Enter player name => ")
        self.gameData.player = Player(name.upper())
        self.gameData.roundEnabled = True
        return True


class ContinueGameCommand(Command):
    def __init__(self, title, gameData):
        super().__init__(title)
        self.gameData = gameData

    def execute(self):
        if self.gameData.player is not None:
            return True
        else:
            raise ValueError("can't continue games without a player")
            return False

        self.gameData.roundEnabled = True
        return True


class HighscoreBoardCommand(Command):
    def __init__(self, title):
        super().__init__(title)
        self.highscoreBoard = HighscoreBoard()

    def execute(self):
        print(self.highscoreBoard)


class HelpCommand(Command):
    def __init__(self, title):
        super().__init__(title)
        self.help = Help()

    def execute(self):
        print(self.help)
        input("\nany key to return to Menu")
