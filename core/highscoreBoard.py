from .save.jsonSave import JsonSave
from .titleVisualizer import TitleVisualizer
import os


class HighscoreBoard:
    def __init__(self):
        self.header = TitleVisualizer("Highscores")
        self.recordSize = 10

    def __repr__(self):
        os.system("cls")
        result = str(self.header)
        result += "\n"
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
            left = '{:.<17}'.format(str(lead + 1) + "." + entry[0])
            right = '{:.>18}'.format(entry[1])
            result += left + right
            result += "\n"
        return result
