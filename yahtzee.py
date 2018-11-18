#! /usr/bin/python
# ------------------------------------------------------------#
# Simple Yahtzee game where you roll and hold dice            #
# to score rolls against a score sheet                        #
# ------------------------------------------------------------#

__author__ = "Paul Lombard"
__version__ = "0.0.1"
__title__ = "Yahtzee"

from core import Turn
from core.gameData import GameData
from core.menu import Menu
from core.debrief import Debrief
import os
import sys


class Game:
    def __init__(self):
        self.data = GameData("devmode" in sys.argv)
        self.menu = Menu(self.data)
        self.turn = Turn(self.data)
        self.debrief = Debrief(self.data)

        self.gameLoop()

    def gameLoop(self):
        """The heart beat of the game.
        game loops on rounds and while the game is enabled"""

        while self.data.gameEnabled:
            self.menu.enter()
            if self.data.roundEnabled:
                # player may choose to quit game from menu
                while self.data.player.scoreSheet.hasScoresToFill():
                    self.turn.enter()
                    if not self.data.roundEnabled:
                        break
                    # self.data.player.waitForAnyKey()

                if self.data.player.scoreSheet.complete():
                    self.debrief.enter()

        print("Game Over!")
        self.clearScreen()

    def clearScreen(self):
        os.system("cls")


if __name__ == "__main__":
    Game()
