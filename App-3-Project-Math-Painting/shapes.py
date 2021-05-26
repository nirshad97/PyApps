

class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.side + self.x, self.y:self.side + self.y] = self.color
        canvas.make()


class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.height + self.x, self.y:self.width + self.y] = self.color
        canvas.make()