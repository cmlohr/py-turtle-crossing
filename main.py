from turtle import Screen, Turtle
from player import TurtlePlayer
# from cars import CarManager
# from score import Score

import time
from art import Art
from plants import Plants


screen = Screen()
screen.bgcolor("#39721D")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = TurtlePlayer()
# cars = CarManager()
# score = Score()
art = Art()
plants = Plants()


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
