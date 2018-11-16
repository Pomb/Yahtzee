import random

class d6:
    """A single instance of a d6 die"""
    def __init__(self):
        self.number = 0

    def roll(self):
        self.number = random.randint(1, 6)
        return self.number

    def __repr__(self):
        if self.number == 0:
            return " "
        else:
            return str(self.number)

class d6Set:
    def __init__(self):
        self.dice = []
        self.hold = []

        for i in range(1,6):
            self.dice.append(d6())
            self.hold.append(False)

    def roll(self):
        for i in range(5):
            if self.hold[i] == False:
                self.dice[i].roll()

    def total(self):
        total = 0
        for i in range(len(self.dice)):
            total += self.dice[i].number
        return total

    def totalForNumber(self, number):
        for i in range(len(self.dice)):
            if self.dice[i].number == number:
                total += number
        return total

    def diceNumbers(self):
        numbers = []
        for d in self.dice:
            numbers.append(d.number)
        return numbers

    def __repr__(self):
        result = ""
        for i in range(5):
            if not self.hold[i]:
                result += " ___ "
            else:
                result += "     "
        result += "\n"
        for i in range(5):
            if not self.hold[i]:
                result += "| "
                result += self.dice[i].__repr__()
                result += " |"
            else:
                result += "  "
                result += self.dice[i].__repr__()
                result += "  "
        result += "\n"
        for i in range(5):
            if not self.hold[i]:
                result += " ̅ ̅ ̅  "
            else:
                result += "     "
        return result

    def getRollableDiceIndices(self):
        subset = []
        for i in self.hold:
            if self.hold[i] == False:
                subset.append(i);
        return subset
