from turtle import Turtle



class Art(Turtle):

    def __init__(self):
        super().__init__()
        self.pave()

    def pave(self):
        berm = Turtle()
        berm.shape("square")
        berm.color("#454955")
        berm.penup()
        berm.shapesize(stretch_wid=25, stretch_len=30)
        berm.goto(0, 0)

        strip = Turtle()
        strip.shape("square")
        strip.color("white")
        strip.penup()
        strip.shapesize(stretch_wid=24, stretch_len=30)
        strip.goto(0, 0)

        road = Turtle()
        road.shape("square")
        road.color("grey")
        road.penup()
        road.shapesize(stretch_wid=23.5, stretch_len=30)
        road.goto(0, 0)

        center_line = Turtle()
        center_line.shape("square")
        center_line.color("white")
        center_line.penup()
        center_line.shapesize(stretch_wid=.2, stretch_len=30)
        center_line.goto(0, 0)

