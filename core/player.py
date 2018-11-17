#! /usr/bin/python
from .scoreSheet import ScoreSheet


class Player:
    def __init__(self):
        self.name = ""
        self.scoreSheet = ScoreSheet()

    def newScoreSheet(self):
        self.scoreSheet = ScoreSheet()

    def waitForAnyKey(self):
        input("\nany key to continue")
