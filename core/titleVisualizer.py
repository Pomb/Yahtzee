class TitleVisualizer:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        #return("    ---> {} <---".format(self.title))
        return self.title.center(30, '=')
