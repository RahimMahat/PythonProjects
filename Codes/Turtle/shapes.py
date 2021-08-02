#!/usr/bin/env python3

from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("DeepSkyBlue4")

turtle_colors = ["CornflowerBlue", "DeepSkyBlue5", "DarkOrchid", "IndianRed", "LightSeaGreen",
                 "wheat","SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(turtle_colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()