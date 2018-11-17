class TitleVisualizer:
    def __init__(self, title, fill='─', width=35):
        self.title = title
        self.fill = fill
        self.width = width

    def __repr__(self):
        # return("    ---> {} <---".format(self.title))
        result = "┌" + (self.width - 2) * self.fill + "┐\n"
        result += "│" + self.title.center(self.width - 2, " ") + "│\n"
        result += "└" + (self.width - 2) * self.fill + "┘"
        return result
