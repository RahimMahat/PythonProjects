#!/usr/bin/env python3
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
# creating screen shape as image
image = "blank_states_img.gif"
screen.addshape(image)
# load up image as our turtle shape
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name? ").title()
    if answer_state == "Exit":
        # states that missed by the user
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break
    # if answer_state is one of the states in all the states of the  50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # if they got it then create a turtle to write name of state and goto x and y co-ordinates
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)       # or state_data.state.item()



'''
# getting co-ordinates of the states from mouse click
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
# mainloop will keep the turtle screen on even after we click
turtle.mainloop()
'''

