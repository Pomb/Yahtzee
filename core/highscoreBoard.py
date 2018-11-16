from .jsonSave import JsonSave
from .titleVisualizer import TitleVisualizer
import os

class HighscoreBoard:
    def __init__(self):
        self.header = TitleVisualizer("Highscores")
        self.recordSize = 10

    def printBoard(self):
        os.system("cls")
        print(self.header)
        data = JsonSave().load()
        scorelist = []
        namelist = []
        for k, v in data.items():
            for s in v:
                scorelist.append(s)
                namelist.append(k)

        zipped = zip(namelist, scorelist)
        bestsort = sorted(zipped, key=lambda tup: tup[1], reverse=True)
        best = bestsort[:self.recordSize]

        for lead, entry in enumerate(best):
            left = '{:.<14}'.format(str(lead + 1) + "." + entry[0])
            right = '{:.>14}'.format(entry[1])
            print(left + right)
        print("\n")
