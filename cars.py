from turtle import Turtle
import random

COLORS = ["#424651", "#AF3B6E", "#377771", "#FFBF00", "#F5AC72", "#ADAABF"]
STARTING_DISTANCE = 5



class CarManager:

    def __init__(self):
        self.all_cars = []

    def make_car(self):
        random_car = random.randint(1, 6)
        if random_car == 1:
            rand_y = random.randint(-200, 200)
            car = Turtle(shape="square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(350, rand_y)
            self.all_cars.append(car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(STARTING_DISTANCE)
