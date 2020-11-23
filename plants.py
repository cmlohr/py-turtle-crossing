from turtle import Turtle

BUSHES = [(-285, -265), (-285, -285), (-275, -280), (-265, -265), (-275, -270), (275, 280), (285, 265),
          (285, 285), (-240, -280), (235, -265), (-225, -285), (-215, -280), (-185, -265), (-205, -285), (-135, -280),
          (105, -265), (235, -285), (75, -280), (85, -265), (115, -285), (59, -280), (87, -265),
          (185, -285), (213, -280), (105, -265), (85, -285), (40, -280), (290, -265), (97, -285),
          (-175, -280), (-159, -265), (150, -285), (75, -280)]


class Plants(Turtle):

    def __init__(self):
        super().__init__()
        self.plant_seeds()

    def plant_seeds(self):
        for position in BUSHES:
            self.grow(position)

    def grow(self, position):
        bush = Turtle(shape="circle")
        bush.color("#214111")
        bush.penup()
        bush.shapesize(stretch_wid=2, stretch_len=2)
        bush.goto(position)