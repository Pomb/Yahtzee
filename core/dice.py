import random


class d6:
    """A single instance of a d6 die"""

    def __init__(self):
        self.number = 0

    def roll(self):
        self.number = random.randint(1, 6)
        return self.number

    def __repr__(self):
        if self.number is 0:
            return " "
        else:
            return str(self.number)


class d6Set:
    def __init__(self):
        self.dice = []
        self.hold = []
        self.numberOfDice = 5
        self.rollCount = 0

        for i in range(self.numberOfDice):
            self.dice.append(d6())
            self.hold.append(False)

    def roll(self):
        for i in range(self.numberOfDice):
            if self.hold[i] is False:
                self.dice[i].roll()
        self.rollCount += 1

    def total(self):
        total = 0
        for i in range(self.numberOfDice):
            total += self.dice[i].number
        return total

    def diceNumbers(self):
        numbers = []
        for d in self.dice:
            numbers.append(d.number)
        return numbers

    def __repr__(self):
        """return dice layout string"""
        result = ""
        for i in range(5):
            if not self.hold[i]:
                result += "┌─────┐"
            else:
                result += "       "
        result += "\n"
        for i in range(5):
            if not self.hold[i]:
                result += "│  "
                result += self.dice[i].__repr__()
                result += "  │"
            else:
                result += "   "
                result += self.dice[i].__repr__()
                result += "   "
        result += "\n"
        for i in range(5):
            if self.hold[i] is False:
                result += "└─────┘"
            else:
                result += "       "
        result += "\n"
        paddedRollCount = " " + str(self.rollCount) + " "
        result += paddedRollCount.center(35, "─")
        return result

    def getRollableDiceIndices(self):
        rollable = []
        for i in range(len(self.hold)):
            if self.hold[i] is False:
                rollable.append(i)
        return rollable
