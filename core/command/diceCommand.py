from .command import Command


class DiceCommand(Command):
    """Base command for dealing with the diceSet"""

    def __init__(self, title, diceSet):
        self.diceSet = diceSet
        self.title = title


class RollCommand(DiceCommand):
    def __init__(self, title, diceSet):
        super().__init__(title, diceSet)

    def execute(self):
        self.diceSet.roll()
        return True


class HoldCommand(DiceCommand):
    def __init__(self, title, diceSet, index):
        super().__init__(title, diceSet)
        self.index = index

    def execute(self):
        self.diceSet.hold[self.index] = True
        print("holding dice index {} ".format(self.index))
        return True


class HoldAllCommand(DiceCommand):
    def __init__(self, title, diceSet):
        super().__init__(title, diceSet)

    def execute(self):
        for i in range(len(self.diceSet.hold)):
            self.diceSet.hold[i] = True
        print(self.title + " dice")
        return True


class ScoreCommand(DiceCommand):
    def __init__(self, title, diceSet, scoreSheet, scoreKey):
        super().__init__(title, diceSet)
        self.scoreSheet = scoreSheet
        self.scoreKey = scoreKey

    def execute(self):
        total = self.scoreSheet.keyTotal(self.scoreKey, self.diceSet)
        self.scoreSheet.addScore(self.scoreKey, total)
        return True
