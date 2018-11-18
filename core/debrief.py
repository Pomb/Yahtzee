from .titleVisualizer import TitleVisualizer
from .command import command as cmd
import os


class Debrief:
    def __init__(self, gameData):
        self.data = gameData

    def enter(self):
        self.clearScreen()
        print(TitleVisualizer("Debrief"))

        score = self.data.player.scoreSheet.total()
        scoreStr = "Total Score " + str(score).center(5, ' ')
        print(TitleVisualizer(scoreStr, " ", boxed=False))
        self.data.roundEnabled = False

        name = input("\nPlayer name => ")
        self.data.player.name = name.upper()

        if self.data.player is not None and len(name) > 0:
            save = cmd.SaveCommand("Save", self.data.player)
            save.execute()
            self.data.player.newScoreSheet()
            self.data.player.waitForAnyKey()

        self.clearScreen()

    def clearScreen(self):
        os.system("cls")
