#!/usr/bin/env python3
import time
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# Player class constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
# CarManager class constants
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# ScoreBoard class constant
FONT = ("Courier", 24, "normal")


# TODO: 1. Create and move the turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)


# TODO: 2. Create and move the cars
class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


# TODO: Create scoreboard
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over ", align="center", font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

car_manager = CarManager()

score_board = ScoreBoard()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # TODO: 3.Detect collision of turtle with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score_board.game_over()

    # TODO: 4.Detect when turtle reaches other side and increase speed as level up
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()
