# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

# Allow RGB values from 0 to 255
turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (234, 226, 211),
    (193, 61, 19),
    (212, 154, 93),
    (217, 218, 226),
    (141, 144, 155),
    (97, 105, 137),
    (230, 212, 107),
    (193, 158, 26),
    (234, 216, 224),
    (208, 150, 177),
    (91, 113, 181),
    (35, 38, 15),
    (19, 28, 71),
    (226, 233, 227),
    (224, 168, 199),
    (25, 42, 23),
    (194, 23, 3),
    (36, 49, 106),
    (207, 94, 64),
    (234, 205, 9),
    (236, 173, 158),
    (111, 97, 106),
    (181, 186, 212),
    (90, 101, 91),
    (155, 164, 156),
    (210, 88, 115),
    (73, 72, 39),
    (43, 26, 41),
    (53, 71, 54),
    (109, 40, 53)
]

# Move turtle to starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # After every 10 dots, move to next row
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()