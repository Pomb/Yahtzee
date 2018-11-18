from .saveStrategy import SaveStrategy
import sqlite3


class DatabaseSave(SaveStrategy):
    def __init__(self):
        self.connection = sqlite3.connect("saves/saveDatabase.db")
        self.cursor = self.connection.cursor()

        self.createTable()

    def load(self):
        pass

    def save(self, player):
        name = player.name
        score = player.scoreSheet.total()
        self.dataEntry(name, score)
        self.closeConnection()

    def closeConnection(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def createTable(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS scoreToAdd(player TEXT, value REAL)')

    def dataEntry(self, name, score):
        self.cursor.execute(
            'INSERT INTO scoreToAdd(player, value) VALUES (?, ?)',
            (name, score))
