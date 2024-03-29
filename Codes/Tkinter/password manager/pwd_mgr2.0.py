#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from random import sample
import pyperclip
import json

# TODO: PASSWORD GENERATOR


def password_generator():
    Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "1234567890"
    symbol = "~!@#$%^&*_+:;<>?`"
    all = Upper + lower + digits + symbol
    length = 17

    password = "".join(sample(all, length))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# TODO: MANAGING CREDENTIALS
def save():
    username = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading from existing file
                data = json.load(data_file)
        except FileNotFoundError:
            # if file not found creating file and dumping data into it
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_creds():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            paswd = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {paswd}")
        else:
            messagebox.showwarning(
                title="Warning", message=f"No details found for {website} in current data file")


# TODO: UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# creating canvas
canvas = Canvas(width=225, height=225)
# loading up image
# image size = 225x225
key_lock_img = PhotoImage(file="lock_logo.png")
# creating image inside canvas
canvas.create_image(125, 110, image=key_lock_img)
canvas.grid(column=1, row=0)

# All labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# All Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1,)
# it'll automatically load the app with cursor on website entry
website_entry.focus()
email_entry = Entry(width=30)
# it'll populate the email entry with preloaded string
email_entry.insert(0, "example@example.com")
email_entry.grid(row=2, column=1, )
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# All Buttons
search_button = Button(text="Search", width=13, command=find_creds)
search_button.grid(row=1, column=2)
generate_password_button = Button(
    text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
