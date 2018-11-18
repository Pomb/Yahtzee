#! /usr/bin/python
from core.save import DatabaseSave
from core.save import JsonSave
import os


def migrate():
    """Copy all data from the json save file into the database"""
    database = DatabaseSave()
    jsonSaves = JsonSave()

    scoreData = jsonSaves.load()

    for name, scores in scoreData.items():
        for score in scores:
            print("{} {}".format(name, score))
            database.dataEntry(name, score)
        os.system('cls')

    database.closeConnection()
    print("migration comlpete")


if __name__ == "__main__":
    migrate()
