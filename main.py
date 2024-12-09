import random
from random import randint
from tkinter import *
from tkinter import messagebox

BG = "#EEEEEE"
PURPLE = "#3B1E54"
LIGHT_PURPLE = "#9B7EBD"

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    with open("data.txt", mode="a") as data_file:
        data_file.write(f"{website} | {username} | {password}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo(title="Password Manager", message="Saved!")

    website_entry.focus()

def random_password():

    random_length = randint(10, 15)
    password = []
    for num in range(random_length):
        if random_length - num > 10:
            random_alpha = chr(randint(65, 90))
            password.append(random_alpha)
        if random_length - num < 10:
            random_lower = chr(randint(97, 122))
            password.append(random_lower)
        if random_length - num < 5:
            random_num = chr(randint(48, 57))
            password.append(random_num)
        if random_length - num < 3:
            random_special = chr(randint(35, 38))
            password.append(random_special)

    psswrd = ''.join(random.sample(password, len(password)))
    password_entry.delete(0, END)
    password_entry.insert(0, psswrd)

window = Tk()
window.title("Password Manager")
window.config(bg=BG, padx=50, pady=50)

title_label = Label(text="Password Manager", font=("Courier", 20, "bold"), bg=BG, fg=PURPLE)
title_label.config(padx=25)
title_label.grid(column=1, row=0)

canvas = Canvas(width=365, height=365, bg=BG, highlightthickness=0)
Padlock_image = PhotoImage(file="Padlock_Image.png")
canvas.create_image(200, 150, image=Padlock_image)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:", font=("arial", 12, "normal"), bg=BG, fg=PURPLE)
website_label.config(pady=5)
website_label.grid(column=0, row=2)

website_entry = Entry(width=59, font=("arial", 10, "normal"))
website_entry.focus()
website_entry.grid(column=1, row=2, columnspan=2)

username_label = Label(text="Email/Username:", font=("arial", 12, "normal"), bg=BG, fg=PURPLE, pady=10)
username_label.grid(column=0, row=3)

username_entry = Entry(width=59, font=("arial", 10, "normal"))
username_entry.insert(0, "mira.ikechukwu15@gmail.com")
username_entry.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password:", font=("arial", 12, "normal"), bg=BG, fg=PURPLE, pady=6)
password_label.grid(column=0, row=4)

password_entry = Entry(width=43, font=("arial", 10, "normal"))
password_entry.grid(column=1, row=4)

generate_button = Button(text="Generate Password", width=15, fg=BG, bg=LIGHT_PURPLE, command=random_password)
generate_button.grid(column=2, row=4)
generate_button.grid_configure()

add_button = Button(text="Add", width=42, fg=BG, bg=PURPLE, command=save_password)
add_button.grid(row=6, column=1)

window.mainloop()