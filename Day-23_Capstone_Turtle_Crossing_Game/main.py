import time
# import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
loop_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # if random.randint(0, 10) == 1:
    #    car_manager.new_car()
    loop_counter += 1  # Used a loop counter to get a car made every 6th iteration of the loop but the above works too
    if loop_counter == 6:
        car_manager.new_car()
        loop_counter = 0
    car_manager.move_cars()  # Moves all cars along at a certain speed
    for car in car_manager.cars:  # Detects collisions between player and the cars
        if player.distance(car) < 25:
            print("Collision")
            scoreboard.game_over()
            game_is_on = False
    if player.detect_finish():  # Detects if player reaches the finish line and updates the score
        car_manager.level_up()
        scoreboard.level += 1
        scoreboard.update_score()

screen.exitonclick()
