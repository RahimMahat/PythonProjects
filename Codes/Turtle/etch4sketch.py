#!/usr/bin/env python3
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
screen = Screen()

'''
w - move forward
s - move bacckward
d - move left
a - move right
c - clear all and arrow back to home
'''

def move_forward():
    tim.fd(10)


def move_backward():
    tim.backward(10)


def move_left():
    tim.left(45)


def move_right():
    tim.right(45)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# adding listener from the screen
screen.listen()
# listener key(key=), call back function(fun=)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()