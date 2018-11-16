#! /usr/bin/python
import os
import json
import random

class JsonSave:
    def __init__(self):
        self.savePath = "saves/save.json"
        pass

    def load(self):
        with open(self.savePath) as saveData:
            return json.load(saveData)

    def save(self, player):
        totalScore = player.scoreSheet.total()

        data = {}

        if os.path.exists(self.savePath):
            data = self.load()

        if player.name in data:
            data[player.name].append(totalScore)
        else:
            data[player.name] = [totalScore]


        with open(self.savePath, 'w') as saveData:
            json.dump(data, saveData, sort_keys=True, indent=4)

        #print("save complete")
