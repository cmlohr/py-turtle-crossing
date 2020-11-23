from turtle import Turtle

START_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#19310D")
        self.penup()
        self.goto(START_POS)
        self.setheading(90)
