#!/usr/bin/env python3
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("classic")
turtle_colors = ["CornflowerBlue", "DeepSkyBlue", "DarkOrchid", "IndianRed", "LightSeaGreen",
                 "wheat","SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")
for _ in range(150):
    tim.color(random.choice(turtle_colors))
    tim.forward(25)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()