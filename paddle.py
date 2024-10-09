from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.position)

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + 75

        if y_cor < 260:
            self.goto(x_cor, y_cor)

    def move_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - 75

        if y_cor > -260:
            self.goto(x_cor, y_cor)
