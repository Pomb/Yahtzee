import collections


class ScoreRules:
    """Scoring methods return the total score against the provided diceSet"""

    def __init__(self):
        pass

    def ones(self, diceSet):
        """Ones - Score the count of 1s"""
        counter = collections.Counter(diceSet.diceNumbers())
        oneCount = counter[1]
        return oneCount

    def twos(self, diceSet):
        """Twos - Score 2s multiplied by 2"""
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[2]
        return count * 2

    def threes(self, diceSet):
        """Threes - Score 3s multiplied by 3"""
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[3]
        return count * 3

    def fours(self, diceSet):
        """Fours - Score 4s multiplied by 4"""
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[4]
        return count * 4

    def fives(self, diceSet):
        """Fives - Score 5s multiplied by 5"""
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[5]
        return count * 5

    def sixes(self, diceSet):
        """Sixes - Score 6s multiplied by 6"""
        counter = collections.Counter(diceSet.diceNumbers())
        count = counter[6]
        return count * 6

    def threeOfAKind(self, diceSet):
        """Three Of A Kind - 3 of the same number. Score dice sum"""
        return diceSet.total()
        counter = collections.Counter(diceSet.diceNumbers())
        if 3 in counter.values():
            return diceSet.total()
        return 0

    def fourOfAKind(self, diceSet):
        """Four Of A Kind - 4 of the same number. Score dice sum"""
        counter = collections.Counter(diceSet.diceNumbers())
        if 4 in counter.values():
            return diceSet.total()
        return 0

    def fullHouse(self, diceSet):
        """Full House - 3 of a kind and 2 of a kind. Score 25"""
        counter = collections.Counter(diceSet.diceNumbers())
        if 3 in counter.values() and 2 in counter.values():
            return 25
        return 0

    def smallStraight(self, diceSet):
        """Small Straight - 1 2 3 4 5. Score 30"""
        counter = collections.Counter(diceSet.diceNumbers())
        if len(set(counter.values())) == 1:
            if 1 in counter.keys() and 6 not in counter.keys():
                return 30
        return 0

    def largeStraight(self, diceSet):
        """Large Straight - 2 3 4 5 6. Score 40"""
        counter = collections.Counter(diceSet.diceNumbers())
        if len(set(counter.values())) == 1:
            if 6 in counter.keys() and 1 not in counter.keys():
                return 40
        return 0

    def yahtzee(self, diceSet):
        """Yahtzee - 5 of the same number. Score 50"""
        counter = collections.Counter(diceSet.diceNumbers())
        if 5 in counter.values():
            return 50
        return 0

    def chance(self, diceSet):
        """Chance - Total of any combination of dice. Score dice sum"""
        return diceSet.total()

    def __repr__(self):
        result = "\nScore Rules:\n"
        result += "    " + self.ones.__doc__ + "\n"
        result += "    " + self.twos.__doc__ + "\n"
        result += "    " + self.threes.__doc__ + "\n"
        result += "    " + self.fours.__doc__ + "\n"
        result += "    " + self.fives.__doc__ + "\n"
        result += "    " + self.sixes.__doc__ + "\n"
        result += "    " + self.threeOfAKind.__doc__ + "\n"
        result += "    " + self.fourOfAKind.__doc__ + "\n"
        result += "    " + self.fullHouse.__doc__ + "\n"
        result += "    " + self.smallStraight.__doc__ + "\n"
        result += "    " + self.largeStraight.__doc__ + "\n"
        result += "    " + self.yahtzee.__doc__ + "\n"
        result += "    " + self.chance.__doc__
        return result
