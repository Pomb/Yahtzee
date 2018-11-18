from .titleVisualizer import TitleVisualizer
from .scoreRules import ScoreRules
import random


class ScoreSheet:
    def __init__(self):
        self.scores = {
            "ones": -1,
            "twos": -1,
            "threes": -1,
            "fours": -1,
            "fives": -1,
            "sixes": -1,
            "threeOfAKind": -1,
            "fourOfAKind": -1,
            "fullHouse": -1,
            "yahtzee": -1,
            "smallStraight": -1,
            "largeStraight": -1,
            "chance": -1,
        }
        self.header = TitleVisualizer("Scoring")
        self.scoreRules = ScoreRules()

    def total(self):
        totalScore = 0
        for k, v in self.scores.items():
            if self.scores[k] > 0:
                totalScore += v
        return totalScore

    def keyTotal(self, key, diceSet):
        """
        creates the command assosicated with the key
        and returns the total score of the diceSet
        """
        switch = {
            "ones": self.scoreRules.ones,
            "twos": self.scoreRules.twos,
            "threes": self.scoreRules.threes,
            "fours": self.scoreRules.fours,
            "fives": self.scoreRules.fives,
            "sixes": self.scoreRules.sixes,
            "threeOfAKind": self.scoreRules.threeOfAKind,
            "fourOfAKind": self.scoreRules.fourOfAKind,
            "fullHouse": self.scoreRules.fullHouse,
            "yahtzee": self.scoreRules.yahtzee,
            "smallStraight": self.scoreRules.smallStraight,
            "largeStraight": self.scoreRules.largeStraight,
            "chance": self.scoreRules.chance,
        }

        rule = switch.get(key, "invalid")

        if isinstance(rule, str):
            raise ValueError("{} key does not exsist")

        total = rule(diceSet)
        return total

    def hasScoresToFill(self):
        hasScoreSlots = False
        for k, v in self.scores.items():
            if v < 0:
                hasScoreSlots = True
                break
        return hasScoreSlots

    def complete(self):
        if self.hasScoresToFill():
            return False
        return True

    def canScore(self, key):
        return self.scores[key] == -1

    def addScore(self, key, amount):
        self.scores[key] = amount
        print("scored {} on {} ".format(amount, key))

    def fillAvailableWithRandomScores(self):
        for k, v in self.scores.items():
            if self.scores[k] < 0:
                # not a true score for the various score slots
                self.addScore(k, random.randint(0, 30))

    def avaialbleScoreSlots(self):
        scoreSlots = []
        for k, v in self.scores.items():
            if v < 0:
                scoreSlots.append(k)
            else:
                name = k.ljust(32, ".")
                score = str(v).rjust(3, ".")
                scoreSlots.append(name + score)

        totalTitle = "Total".ljust(32, ".")
        total = str(self.total()).rjust(3, ".")
        scoreSlots.append(totalTitle + total)

        return scoreSlots

    def strike(self, text):
        # Dosn't work in normal terminal but works in atom terminal
        return '\u0336'.join(text) + '\u0336'
        # result = ""
        # for c in text:
        #     result = result + c + '\u0336'
        # return result

    def __repr__(self):
        sheet = []
        for k, v in self.scores.items():
            name = k.ljust(32, ".")
            score = str(v).rjust(3, ".")
            sheet.append(name + score)

        totalTitle = "Total".ljust(32, ".")
        total = str(self.total()).rjust(3, ".")
        sheet.append(totalTitle + total)
        return sheet
