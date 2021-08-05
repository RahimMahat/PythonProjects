#!/usr/bin/env python3
import tkinter

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(
    text="I am a label", font=("Times New Roman", 25, "bold"))


my_label.pack()


def button_clicked():
    print("i got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)


# Button
button = tkinter.Button(text="click it", command=button_clicked)
button.pack()
# button.place(x=23, y=34)


# Entry
entry = tkinter.Entry(width=20)
entry.pack()


# Spinbox
def spinbox_action():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_action)
spinbox.pack()


# Scale
def scale_action():
    print()


scale = tkinter.Scale(from_=0, to=100, command=scale_action)
scale.pack()

window.mainloop()
