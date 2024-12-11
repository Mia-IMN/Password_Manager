import pyperclip
from random import randint, shuffle
from tkinter import *
from tkinter import messagebox
import json

BG = "#EEEEEE"
PURPLE = "#3B1E54"
LIGHT_PURPLE = "#9B7EBD"

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_dict = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you don't have any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_dict)


        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)

            messagebox.showinfo(title=website, message="Website details added!")

        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            messagebox.showinfo(title=website, message="Website details added!")

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()

def search():
    website = website_entry.get()
    usernameEntry = username_entry.get()

    if len(website) == 0:
        raise SyntaxError

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except SyntaxError:
        messagebox.showerror(title="Error", message="Please make sure you don't have the website field empty")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Please add website details to use the search functionality")

    else:
        username = [data[datum]["username"] for datum in data if datum == website]
        password = [data[datum]["password"] for datum in data if datum == website]

        #fix this error
        if usernameEntry:
            messagebox.showerror(title="Error", message=f"No details found for {website}")
        else:
            messagebox.showinfo(title=website, message=f"Username: {username[0]}\nPassword: {password[0]}")

    finally:
        website_entry.delete(0, END)
        website_entry.focus()

def random_password():

    password_uppercase = [chr(randint(65, 90)) for _ in range(6, 12)]
    password_lowercase = [chr(randint(97, 122)) for _ in range(5, 12)]
    password_num = [chr(randint(48, 57)) for _ in range(1, 4)]
    password_symbol = [chr(randint(35, 38)) for _ in range(1, 3)]

    password = password_uppercase + password_lowercase + password_num + password_symbol
    shuffle(password)
    new_password = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)

    pyperclip.copy(new_password)

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

website_entry = Entry(width=43, font=("arial", 10, "normal"))
website_entry.focus()
website_entry.grid(column=1, row=2)

search_button = Button(text="Search", width=15, fg=BG, bg=PURPLE, command=search)
search_button.grid(row=2, column=2)

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

add_button = Button(text="Add", width=42, fg=BG, bg=PURPLE, command=save_password)
add_button.grid(row=6, column=1)

window.mainloop()