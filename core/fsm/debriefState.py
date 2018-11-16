from .state import State
from ..titleVisualizer import TitleVisualizer

class DebriefState(State):
    def __init__(self, title, machine, player):
        super().__init__(title, machine)
        self.player = player        
        self.header = TitleVisualizer("Debrief")

    def Enter(self):
        os.system("cls")
        print(self.header)

        self.roundEnabled = False

        if self.player is not None:
            save = SaveCommand("Save", self.player)
            save.execute()

            #score = self.player.scoreSheet.total()
            score = random.randint(40, 300)
            scoreStr = str(score).center(5, ' ')
            print(scoreStr.center(28, '#'))

            self.player.newScoreSheet()
            self.player.waitForAnyKey()
        os.system("cls")
