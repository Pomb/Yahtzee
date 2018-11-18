from .command import command as cmd
from .command import diceCommand as dcmd
from .dice import d6Set
from .titleVisualizer import TitleVisualizer
import os


class Turn:
    def __init__(self, gameData):
        self.gameData = gameData
        self.header = TitleVisualizer("Rolling")
        self.diceSet = None
        self.maxRolls = 3

    def enter(self):
        self.diceSet = d6Set()

        while self.hasRolls():
            if not self.gameData.roundEnabled:
                break
            self.play()

        if self.gameData.roundEnabled:
            self.chooseScore()

    def hasRolls(self):
        hasRoll = self.diceSet.rollCount < self.maxRolls
        if hasRoll:
            return self.hasDiceToHold()
        return hasRoll

    def hasDiceToHold(self):
        rollable = self.diceSet.getRollableDiceIndices()
        return len(rollable) > 0

    def play(self):
        os.system("cls")
        print(self.header)
        print(self.diceSet)

        actions = {}
        actions["r"] = dcmd.RollCommand("Roll", self.diceSet)

        if self.diceSet.rollCount > 0:
            actions["h"] = dcmd.HoldAllCommand("Hold All", self.diceSet)
            for i in range(len(self.diceSet.dice)):
                if self.diceSet.hold[i] is False:
                    actions[str(i + 1)] = dcmd.HoldCommand(
                        "Hold ", self.diceSet, i)

        actions["s"] = cmd.AvaialbleSlotsCommand("Score Slots", self.gameData)
        actions["q"] = cmd.EndRoundCommand("Quit Round", self.gameData)

        if self.gameData.devmode:
            actions["f"] = cmd.FillScoresRandomCommand(
                "Fill With Random Scores", self.gameData)

        actionPrompts = "\n"
        for key, value in actions.items():
            actionPrompts += ("\t{} - {}\n".format(key, value.title))

        validChoice = False
        print(actionPrompts)

        while not validChoice:
            actionChoice = input("Input=> ")
            if actionChoice in actions:
                validChoice = actions[actionChoice].execute()
                print(self.diceSet)
            else:
                print("\nInvalid input, try again")

        if self.hasRolls() is False:
            dcmd.HoldAllCommand("Finished rolling ", self.diceSet).execute()

    def chooseScore(self):
        os.system("cls")
        if not self.gameData.roundEnabled:
            return

        print(self.gameData.player.scoreSheet.header)
        print(self.diceSet)

        actions = {}
        for i, (key, value) in enumerate(
                self.gameData.player.scoreSheet.scores.items()):
            if value < 0:
                actions[str(i + 1)] = dcmd.ScoreCommand(
                    key, self.diceSet, self.gameData.player.scoreSheet, key)

        actionPrompts = "\n"
        for key, value in actions.items():
            actionPrompts += ("\t{} - {}\n".format(key, value.title))

        validChoice = False
        print(actionPrompts)

        while not validChoice:
            scoreChoice = input("Input=> ")
            if scoreChoice in actions:
                validChoice = actions[scoreChoice].execute()
            else:
                print("Invaild input, please try again")

        self.gameData.player.waitForAnyKey()
