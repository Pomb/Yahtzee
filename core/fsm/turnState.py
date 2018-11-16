from .state import State
from ..titleVisualizer import TitleVisualizer
from ..dice import d6Set

class TurnState(State):
    def __init__(self, machine, player):
        self.game = game
        self.header = TitleVisualizer("Rolling")
        self.player = player
        self.diceSet = d6Set()
        self.rollCount = 0
        self.maxRolls = 3

    def hasRolls(self):
        hasRoll = self.rollCount <= self.maxRolls
        if hasRoll:
            rollable = self.diceSet.getRollableDiceIndices()
            if len(rollable) == 0:
                hasRoll = False
        return hasRoll

    def play(self):
        os.system("cls")
        print(self.header)
        print(self.diceSet)

        actions = {}
        hasrolls = self.hasRolls()
        if hasrolls:
            actions["r"] = RollCommand("Roll", self.diceSet)
            if self.rollCount > 0:
                actions["h"] = HoldAllCommand("Hold all", self.diceSet)

                for i in range(len(self.diceSet.dice)):
                    if self.diceSet.hold[i] == False:
                        actions[str(i + 1)] = HoldCommand("Hold ", self.diceSet, i)
        actions["q"] = EndRoundCommand("Quit Round", self.game)

        actionPrompts = "\n"
        for key, value in actions.items():
            actionPrompts += ("\t{} - {}\n".format(key, value.title))

        actionChoice = input(actionPrompts)

        if actionChoice in actions:
            if actions[actionChoice].execute():
                print(self.diceSet)
                if isinstance(actions[actionChoice], HoldCommand):
                    pass
                else:
                    self.rollCount = self.rollCount + 1
        else:
            print("\ninvalid prompt, try again")

        if self.hasRolls() == False:
            HoldAllCommand("Finished rolling ", self.diceSet).execute()

    def chooseScore(self):
        os.system("cls")
        self.player.scoreSheet.titleVisualizer.printTitle()
        print(self.diceSet)

        actions = {}
        for i, (key, value) in enumerate(self.player.scoreSheet.scores.items()):
            if value < 0:
                actions[str(i + 1)] = ScoreCommand(key, self.diceSet, self.player.scoreSheet, key)

        actionPrompts = "\n"
        for key, value in actions.items():
            actionPrompts += ("\t{} - {}\n".format(key, value.title))

        validChoice = False

        while not validChoice:
            scoreChoice = input(actionPrompts)
            if scoreChoice in actions:
                validChoice = actions[scoreChoice].execute()
            else:
                print("Invaild command, please try again")
