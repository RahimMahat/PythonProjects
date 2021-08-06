#!/usr/bin/env python3
from tkinter import *
import math
# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# TODO: TIMER RESET


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")

# TODO: TIMER MECHANISM


def start_timer():    # countdown calls
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 8th reps long_break_sec
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    # if it's the 2nd,4th,6th reps short_break_sec
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    # if it's the 1st,3rd,5th,7th reps work_sec
    else:
        count_down(work_sec)
        title_label.config(text="Work Time", fg=GREEN)


# TODO: COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # configuring canvas item's text
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # after(ms, func, *args). to trigger the given function after given time
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# TODO: UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=70, bg=YELLOW)


# Label
title_label = Label(text="Timer", fg=GREEN,
                    bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas
# image size = 360x360
# creating canvas to put our tomato image in the TKinter window
canvas = Canvas(width=360, height=360, bg=YELLOW, highlightthickness=0)
# providing image by using the photoimage class of TKinter
tomato_img = PhotoImage(file="tomato.png")
# placing the image in the center by providing half the dim. of the image
# create_image(x= , y= , image= )
canvas.create_image(180, 180, image=tomato_img)
# create_text(x= , y= , text= , fill=color, font=tuple)
timer_text = canvas.create_text(180, 190, text="00:00", fill="white",
                                font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)


# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# check marks
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
