#!/usr/bin/env python3
import turtle
from turtle import Turtle, Screen
import time
import random

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #  TODO: 1.Create a snake body
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    #  TODO: 2.Move the snake
    def move(self):
        #   range(start=, stop=, step=)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # to follow the previous block of snake piece to the next of it
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # now as first piece move anywhere then the previous pieces will follow it's lead
        self.segments[0].forward(MOVE_DISTANCE)

    #  TODO: 3.Control the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # TODO: 5.Extend the snake when eat food
    def extend(self):
        self.add_segment(self.segments[-1].position())


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # creating 10 x 10 food
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("magenta")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class ScoreBoard(Turtle):
    # TODO: 6.Create a score board
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


############################################################################################

screen = Screen()
# setting up screen size
screen.setup(width=600, height=600)
# background colour
screen.bgcolor("black")
# title to the window
screen.title("Snake Game")
# turning off the tracer to stop distance animation
# to get the animation clearly back we'll use update method in snake class
screen.tracer(0)

# creating object of snake class to start the game
snake = Snake()
# creating food object of food class
food = Food()
# creating score-board object from ScoreBoard class
score_board = ScoreBoard()

# listening for the keys to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

level = turtle.textinput(title="Choose level", prompt="easy(e),hard(h),expert(i)")
game_is_on = True
while game_is_on:
    # updating the screen animation after moving the pieces, so we don't see it breaking
    screen.update()
    if not level:
        game_is_on = False
    # sleep time will define the snake's speed indirectly
    if level == "e":
        time.sleep(0.5)
    elif level == "h":
        time.sleep(0.1)
    elif level == "i":
        time.sleep(0.05)

    snake.move()

    # TODO: 4.Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score_board.increase_score()

    # TODO: 7.Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # TODO: 8.Detect collision with body
    for segment in snake.segments[1:]:
        # if head collides with any segment in the body of snake except head, then triggers game_over
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
