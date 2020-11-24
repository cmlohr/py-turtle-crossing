from turtle import Screen, Turtle
from player import TurtlePlayer
from cars import CarManager
from score import Score
import time
from art import Art
from plants import Plants

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

art = Art()
plants = Plants()
cars = CarManager()
player = TurtlePlayer()
score = Score()

screen.listen()
screen.onkey(player.up, "Up")

car_speed = 0.1
game_on = True
while game_on:
    time.sleep(car_speed)
    screen.update()
    cars.make_car()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(player) < 18:
            score.game_over()
            game_on = False

    if player.ycor() > 220:
        car_speed *= 0.6
        score.new_level()
        player.reset()
#
screen.exitonclick()
