#!/usr/bin/env python3
from functools import lru_cache
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()


def random_color():
    color_list = []
    lru_cache(maxsize=5)
    for _ in range(30):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_tuple = (r, g, b)
        color_list.append(color_tuple)
    return color_list


tim.setheading(225)
tim.forward(350)
tim.setheading(0)
number_of_dots = 100


for dot_counts in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(random_color()))
    tim.fd(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50*10)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()