class TitleVisualizer:
    def __init__(self, title, fill='─', width=35, boxed=True):
        self.title = title
        self.fill = fill
        self.width = width
        self.boxed = boxed

    def __repr__(self):
        # return("    ---> {} <---".format(self.title))
        result = ""
        if self.boxed:
            result = "┌" + (self.width - 2) * self.fill + "┐\n│"
        result += self.title.center(self.width - 2, " ")
        if self.boxed:
            result += "│\n└" + (self.width - 2) * self.fill + "┘"
        return result
