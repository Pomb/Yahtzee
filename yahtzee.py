#! /usr/bin/python
# ------------------------------------------------------------#
# Simple Yahtzee game where you roll and hold dice            #
# to score rolls against a score sheet                        #
# ------------------------------------------------------------#

__author__ = "Paul Lombard"
__version__ = "0.0.1"
__title__ = "Yahtzee"

from core import Turn
from core import TitleVisualizer
from core.command import command as cmd
from core.gameData import GameData
import os
import collections


class Game:
    def __init__(self):
        self.data = GameData()
        self.gameLoop()

    def gameLoop(self):
        os.system("Yahtzee Console Game")

        while self.data.gameEnabled:
            self.menu()
            if self.data.roundEnabled:
                # player may choose to quit game from menu
                while self.data.player.scoreSheet.hasScoresToFill():
                    turn = Turn(self.data)
                    while(turn.hasRolls()):
                        turn.play()
                        if not self.data.roundEnabled:
                            break
                    if not self.data.roundEnabled:
                        break
                    turn.chooseScore()
                    self.data.player.waitForAnyKey()

                if self.data.player.scoreSheet.filled():
                    self.debrief()

        print("Game Over!")
        self.clearScreen()

    def menu(self):
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

        choice = input(actionPrompts)

        if choice in actions:
            actions[choice].execute()

    def debrief(self):
        self.clearScreen()
        print(TitleVisualizer("Debrief"))

        score = self.data.player.scoreSheet.total()
        scoreStr = "Total Score " + str(score).center(5, ' ')
        print(TitleVisualizer(scoreStr, " ", boxed=False))
        self.data.roundEnabled = False

        name = input("\nPlayer name => ")
        self.data.player.name = name.upper()

        if self.data.player is not None:
            save = cmd.SaveCommand("Save", self.data.player)
            save.execute()
            self.data.player.newScoreSheet()
            self.data.player.waitForAnyKey()

        self.clearScreen()

    def clearScreen(self):
        os.system("cls")


if __name__ == "__main__":
    game = Game()
