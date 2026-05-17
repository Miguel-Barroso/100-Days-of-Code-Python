# import colorgram
#
# color_objects = colorgram.extract("image.jpg", 30)
#
# color_list = []
# rgb_tuple = ()
#
# for colors in color_objects:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     rgb_tuple = (r, g, b)
#     color_list.append(rgb_tuple)
#
# print(color_list)

color_list = [(193, 171, 145), (214, 218, 221), (214, 219, 216), (218, 214, 216), (140, 172, 184), (216, 202, 135),
              (62, 114, 133), (144, 180, 142), (143, 90, 76), (14, 58, 80), (62, 127, 101), (107, 78, 86),
              (198, 98, 74), (78, 147, 165), (171, 153, 160), (175, 157, 56), (10, 61, 50), (202, 187, 184),
              (10, 84, 101), (74, 167, 146), (157, 205, 217), (169, 103, 111), (37, 64, 96), (68, 44, 35), (44, 33, 35),
              (160, 32, 38), (178, 201, 185), (209, 177, 180), (15, 96, 81)]

# TODO 1. Paint 10 x 10 rows of spots
# TODO 2. Make spots 20px in size and spaced 50 paces apart
# TODO 3. Should paint from left to right, from lowest row going up

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.speed(0)

x = -225
y = -250


def get_random_color():
    random_color = random.choice(color_list)
    tim.color(random_color)
    tim.fillcolor(random_color)


def draw_dot():
    tim.pendown()
    tim.begin_fill()
    tim.circle(10)  # Diameter is 20
    tim.end_fill()
    tim.penup()


def draw_row(x_coordinate, y_coordinate):
    for _ in range(10):
        tim.teleport(x_coordinate, y_coordinate)
        get_random_color()
        draw_dot()
        tim.forward(50)
        x_coordinate += 50


for _ in range(10):
    draw_row(x, y)
    y += 50

screen = t.Screen()
screen.exitonclick()
