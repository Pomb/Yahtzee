class GameData:
    def __init__(self, devmode):
        self.gameEnabled = True
        self.roundEnabled = False
        self.player = None
        self.devmode = devmode

        if devmode:
            input("DEV MODE ACTIVATED!")
