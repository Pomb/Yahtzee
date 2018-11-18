class TitleVisualizer:
    def __init__(self, title, fill='─', width=35, boxed=True):
        self.title = title
        self.fill = fill
        self.width = width
        self.boxed = boxed
        self.NE = "┐"
        self.NW = "┌"
        self.SW = "└"
        self.SE = "┘"
        self.W = "│"
        self.E = "│"

    def __repr__(self):
        result = ""
        if self.boxed:
            result = self.NW + (self.width - 2) * self.fill
            result += self.NE + "\n" + self.W

        result += self.title.center(self.width - 2, " ")

        if self.boxed:
            result += self.E + "\n" + self.SW
            result += (self.width - 2) * self.fill + self.SE

        return result
