import collections

class ScoreRules:
    """Scoring methods return the total score against the provided diceSet"""
    def __init__(self):
        pass

    def ones(self, diceSet):
        counter = collections.Counter(diceSet.diceNumbers())
        oneCount = counter[1]
        return oneCount

    def twos(self, diceSet):
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[2]
        return count * 2

    def threes(self, diceSet):
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[3]
        return count * 3

    def fours(self, diceSet):
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[4]
        return count * 4

    def fives(self, diceSet):
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[5]
        return count * 5

    def sixes(self, diceSet):
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[6]
        return count * 6

    def threeOfAKind(self, diceSet):
        return diceSet.total()
        counter = collections.Counter(diceSet.diceNumbers())
        if 3 in counter.values():
            return diceSet.total()
            # for k, v in counter.items():
            #     if(v == 3):
            #         return k * 3
        return 0

    def fourOfAKind(self, diceSet):
        counter = collections.Counter(diceSet.diceNumbers())
        if 4 in counter.values():
            return diceSet.total()
            # for k, v in counter.items():
            #     if(v == 4):
            #         return k * 4
        return 0

    def fullHouse(self, diceSet):
        """3 of a kind and 2 pair"""
        counter = collections.Counter(diceSet.diceNumbers())
        if 3 in counter.values() and 2 in counter.values():
            return 25
        return 0

    def smallStraight(self, diceSet):
        """1 2 3 4 5"""
        counter = collections.Counter(diceSet.diceNumbers())
        if len(set(counter.values())) == 1:
            if 1 in counter.keys() and 6 not in counter.keys():
                return 30
        return 0

    def largeStraight(self, diceSet):
        """2 3 4 5 6"""
        counter = collections.Counter(diceSet.diceNumbers())
        if len(set(counter.values())) == 1:
            if 6 in counter.keys() and 1 not in counter.keys():
                return 40
        return 0

    def yahtzee(self, diceSet):
        """5 of the same number"""
        counter = collections.Counter(diceSet.diceNumbers())
        if 5 in counter.values():
            return 50
        return 0

    def chance(self, diceSet):
        """Any combination of dice"""
        return diceSet.total()
