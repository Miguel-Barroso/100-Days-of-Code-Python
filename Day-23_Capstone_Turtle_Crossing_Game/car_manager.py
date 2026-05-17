import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(300, random.randrange(-250, 250, STARTING_MOVE_DISTANCE))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
