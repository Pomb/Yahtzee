#! /usr/bin/python
from ..jsonSave import JsonSave
from ..player import Player
from ..highscoreBoard import HighscoreBoard

class Command:
    def __init__(self, title):
        self.title = title

    def execute(self):
        """Return command execute success"""
        return True

class SaveCommand(Command):
    def __init__(self, title, player):
        super().__init__(title)
        self.player = player

    def execute(self):
        JsonSave().save(self.player);
        return True

class QuitCommand(Command):
    def __init__(self, title, game):
        super().__init__(title)
        self.game = game

    def execute(self):
        self.game.data.gameEnabled = False
        self.game.data.roundEnabled = False
        return True

class EndRoundCommand(Command):
    def __init__(self, title, game):
        super().__init__(title)
        self.game = game

    def execute(self):
        self.game.data.roundEnabled = False
        return True

class NewGameCommand(Command):
    def __init__(self, title, game):
        super().__init__(title)
        self.game = game

    def execute(self):
        name = input("Enter player name => ")
        self.game.data.player = Player(name.upper())
        self.game.data.roundEnabled = True
        return True

class ContinueGameCommand(Command):
    def __init__(self, title, game):
        super().__init__(title)
        self.game = game

    def execute(self):
        name = ""
        if self.game.data.player is not None:
            name = self.data.game.player.name
        else:
            raise ValueError("can't continue games without a player")
        self.game.data.roundEnabled = True
        return True

class HighscoreBoardCommand(Command):
    def __init__(self, title):
        super().__init__(title)
        self.highscoreBoard = HighscoreBoard()

    def execute(self):
        self.highscoreBoard.printBoard()
