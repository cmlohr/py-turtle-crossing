from turtle import Screen, Turtle
from player import Player
from cars import CarManager
from score import Score
import time

screen = Screen()
player = Player()
cars = CarManager()
score = Score()
screen.setup(width=600, height=600)
screen.tracer(0)






game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

