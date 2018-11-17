#! /usr/bin/python
from .scoreSheet import ScoreSheet


class Player:
    def __init__(self, name):
        self.name = name
        self.scoreSheet = ScoreSheet()

    def newScoreSheet(self):
        self.scoreSheet = ScoreSheet()

    def waitForAnyKey(self):
        input("any key to continue")
