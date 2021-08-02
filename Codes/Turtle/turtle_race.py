#!/usr/bin/env python3
from turtle import Turtle, Screen
import random


# setting up the screen according to our need
screen = Screen()
screen.setup(width=500, height=400)
user_turtle = screen.textinput(title="Choose the winner turtle by colour", prompt="Enter any colour from Rainbow")

all_turtles = []
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70,-40,-10,20,50,80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(rainbow_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)


race_on = False
if user_turtle:
    race_on = True
while race_on:
    
    for turtle in all_turtles:
        # check to see if any turtle reach the finishing line
        # turtle icon takes the 40px so (250-20), so waiting for  any turtle to cross the finish line
        if turtle.xcor() > 230:
            race_on = False
            # getting winner turtle's colour
            winning_color = turtle.pencolor()
            if winning_color == user_turtle:
                print(f"Congrats, {winning_color} turtle won!!! ")
            else:
                print(f"Sorry, you've lost {winning_color} turtle is the winner")
        # race starts
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()