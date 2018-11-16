from .titleVisualizer import TitleVisualizer
from .command import *
from .scoreRules import ScoreRules

class ScoreSheet:
    def __init__(self):
        self.scores = {
            "ones" : -1,
            "twos" : -1,
            "threes" : -1,
            "fours" : -1,
            "fives" : -1,
            "sixes" : -1,
            "threeOfAKind" : -1,
            "fourOfAKind" : -1,
            "fullHouse" : -1,
            "yahtzee" : -1,
            "smallStraight" : -1,
            "largeStraight" : -1,
            "chance" : -1,
            }
        self.header = TitleVisualizer("Scoring")
        self.scoreRules = ScoreRules()

    def total(self):
        totalScore = 0
        if not self.hasScoresToFill():
            for k, v in self.scores.items():
                totalScore += v
        return totalScore

    def keyTotal(self, key, diceSet):
        """creates the command assosicated with the key and returns the total score"""
        switch = {
            "ones" : self.scoreRules.ones,
            "twos" : self.scoreRules.twos,
            "threes" : self.scoreRules.threes,
            "fours" : self.scoreRules.fours,
            "fives" : self.scoreRules.fives,
            "sixes" : self.scoreRules.sixes,
            "threeOfAKind" : self.scoreRules.threeOfAKind,
            "fourOfAKind" : self.scoreRules.fourOfAKind,
            "fullHouse" : self.scoreRules.fullHouse,
            "yahtzee" : self.scoreRules.yahtzee,
            "smallStraight" : self.scoreRules.smallStraight,
            "largeStraight" : self.scoreRules.largeStraight,
            "chance" : self.scoreRules.chance,
        }

        rule = switch.get(key, "invalid")

        #if the rule isn't a delegate from the dictionary
        #somethings gone wrong and it's invalid
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

    def filled(self):
        if self.hasScoresToFill():
            return False
        return True;

    def canScore(self, key):
        return self.scores[key] == -1

    def addScore(self, key, amount):
        self.scores[key] = amount
        print("scored {} on {} ".format(amount, key))
