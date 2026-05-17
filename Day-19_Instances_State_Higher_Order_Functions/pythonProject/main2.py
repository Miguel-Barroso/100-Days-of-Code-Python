import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False  # Prevents while loop from starting prematurely

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

if user_bet:
    is_race_on = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-100, -60, -20, 20, 60, 100]
names = ["tim", "tom", "tony", "ted", "theo", "terry"]
all_turtles = []


def create_turtle_object(name, color, y_coordinate):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate)
    new_turtle.color(color)
    new_turtle.name = name  # Not needed but thought it was cool
    all_turtles.append(new_turtle)
    # print(name, color, y_coordinate) For debugging purposes


for turtle_index in range(0, 6):
    create_turtle_object(name=names[turtle_index], color=colors[turtle_index], y_coordinate=y_coordinates[turtle_index])

# print(all_turtles)  Prints a list of objects for debugging purposes

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! You guessed right! {turtle.name.title()} the {turtle.pencolor()} turtle won!")
            else:
                print(f"Race is over! {turtle.name.title()} the {turtle.pencolor()} turtle won, however you lose!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
