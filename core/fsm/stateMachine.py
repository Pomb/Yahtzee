class StateMachine:
    def __init__(self):
        self.current = None

    def transition(self, state):
        if self.current is not None:
            self.current.Exit()
        self.current = state
        self.current.Enter()

    def Update(self):
        current.Update
