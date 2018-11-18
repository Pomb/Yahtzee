#! /usr/bin/python
from ..save import JsonSave
from ..save import DatabaseSave
from ..player import Player
from ..highscoreBoard import HighscoreBoard
from ..help import Help
from ..exceptions import NoPlayerError


class Command:
    """Base command"""

    def __init__(self, title):
        self.title = title

    def execute(self):
        """Return command execution success"""
        return True


class SaveCommand(Command):
    def __init__(self, title, player, saveStrategy="json"):
        super().__init__(title)
        self.stratgyTypes = {"json": JsonSave(), "database": DatabaseSave()}
        self.player = player
        self.saveStrategy = saveStrategy

    def execute(self):
        if self.saveStrategy in self.stratgyTypes:
            self.stratgyTypes[self.saveStrategy].save(self.player)
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
        self.gameData.player = Player()
        self.gameData.roundEnabled = True
        return True


class ContinueGameCommand(Command):
    def __init__(self, title, gameData):
        super().__init__(title)
        self.gameData = gameData

    def execute(self):
        if self.gameData.player is None:
            raise NoPlayerError("game requires a player")
            return False

        self.gameData.roundEnabled = True
        return True


class HighscoreBoardCommand(Command):
    def __init__(self, title):
        super().__init__(title)
        self.highscoreBoard = HighscoreBoard()

    def execute(self):
        print(self.highscoreBoard)
        input("\nany key to return to Menu")
        return True


class HelpCommand(Command):
    def __init__(self, title):
        super().__init__(title)
        self.help = Help()

    def execute(self):
        print(self.help)
        input("\nany key to return to Menu")
        return True


class AvaialbleSlotsCommand(Command):
    def __init__(self, title, gameData):
        super().__init__(title)
        self.gameData = gameData

    def execute(self):
        avaialbleSlots = self.gameData.player.scoreSheet.avaialbleScoreSlots()
        for i in range(len(avaialbleSlots)):
            print(avaialbleSlots[i])
        input("\nany key to return")
        return True


class FillScoresRandomCommand(Command):
    def __init__(self, title, gameData):
        super().__init__(title)
        self.gameData = gameData

    def execute(self):
        self.gameData.player.scoreSheet.fillAvailableWithRandomScores()
        self.gameData.roundEnabled = False
        return True
