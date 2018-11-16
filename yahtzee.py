#! /usr/bin/python
# ------------------------------------------------------------#
# Simple Yahtzee game where you roll and hold dice to make    #
# the scores against a score sheet                            #
# ------------------------------------------------------------#

__author__ = "Paul Lombard"
__version__ = "0.0.1"
__title__ = "Yahtzee"

from core import Turn
from core import TitleVisualizer
from core.command import *
from core.gameData import GameData
import os
import random
import collections

class Game:
    def __init__(self):
        self.data = GameData()
        self.gameLoop()

    def gameLoop(self):
        os.system("cls")

        while self.data.gameEnabled:
            self.menu()
            if self.data.roundEnabled:
                #player may choose to quit game from menu
                while self.data.player.scoreSheet.hasScoresToFill():
                    turn = Turn(self.data.player, self)
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

    def menu(self):
        print(TitleVisualizer("Yahtzee Menu"))

        actions = {
            "1" : NewGameCommand("New Game", self),
            "h" : HighscoreBoardCommand("Highscores"),
            "q" : QuitCommand("Quit Game", self)
        }

        if self.data.player is not None:
            actions["0"] = ContinueGameCommand("Continue As " + self.data.player.name, self)
            actions["1"] = NewGameCommand("New Player Game", self)

        orderedActions = collections.OrderedDict(sorted(actions.items()))

        actionPrompts = "\n"
        for key, value in orderedActions.items():
            actionPrompts += ("\t{} - {}\n".format(key, value.title))

        choice = input(actionPrompts)

        if choice in actions:
            actions[choice].execute()

    def debrief(self):
        os.system("cls")
        print(TitleVisualizer("Debrief"))

        self.data.roundEnabled = False

        if self.data.player is not None:
            save = SaveCommand("Save", self.data.player)
            save.execute()

            #score = self.player.scoreSheet.total()
            score = random.randint(40, 300)
            scoreStr = str(score).center(5, ' ')
            print(scoreStr.center(28, '#'))

            self.data.player.newScoreSheet()
            self.data.player.waitForAnyKey()
        os.system("cls")

if __name__ == "__main__":
    game = Game()
