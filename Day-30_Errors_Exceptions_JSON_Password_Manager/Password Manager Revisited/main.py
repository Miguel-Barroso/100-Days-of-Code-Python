import pyperclip
import random
import json
from tkinter import *  # Imports all classes and constants, but not free floating modules
from tkinter import messagebox  # Module to use system dialogs. NB! Not a class!


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List comprehensions instead of for loops
    # Appends a random choice from the lists above for a randomized range
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, password)  # Need the specify index, then what to insert
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Gets the current entries and generates a string to be saved in a file
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # Data validation
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Data Validation Warning!", message="Don't leave any fields empty!")
    else:
        try:
            # Try and open an existing file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Reads old data (change mode) and saves into a Python Dict
                # print(data)
                data.update(new_data)  # Updates the Python Dict with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:  # Changed from .txt to .json and mode from "a" to "w"
                data = new_data
        finally:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # Saving the updated data
                # Clears the fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    # Data validation
    if len(website) == 0:
        messagebox.showwarning(title="Data Validation Warning!", message="Cannot search for empty website!")
    else:
        try:
            # Try and open an existing file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Reads old data (change mode) and saves into a Python Dict
                if website in data:
                    messagebox.showinfo(title=website, message=f"Email: {data[website]['username']}\nPassword: {data[website]['password']}")
                else:
                    print("No details for the website exists.")
                    messagebox.showwarning(title="Data Retrieval Error", message=f"No details for {website} exists.")
        except FileNotFoundError:
            messagebox.showwarning(title="Data Retrieval Error", message="No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)  # Window width not specified as elements will auto stretch it

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")  # Used to traverse file systems and get hold of an image
canvas.create_image(100, 100, image=logo_image)  # Needs PhotoImage object as input as well as x, y canvas positions
canvas.grid(column=1, row=0, columnspan=2, sticky="EW")

# Labels
website_label = Label(text="Website ")
website_label.grid(column=0, row=1, sticky="E")  # sticky="E" will right-align the labels
username_label = Label(text="Email/Username ")
username_label.grid(column=0, row=2, sticky="E")
password_label = Label(text="Password ")
password_label.grid(column=0, row=3, sticky="E")

# Entries
website_entry = Entry()  # Used to have width=35
website_entry.focus()  # Puts the cursor in this box
website_entry.grid(column=1, row=1, sticky="EW", padx=2, pady=2)
username_entry = Entry()  # Used to have width=35
username_entry.insert(END, "miguel@miguelbarroso.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW", padx=2, pady=2)
password_entry = Entry()  # Used to have width=21
password_entry.grid(column=1, row=3, sticky="EW", padx=2, pady=2)

# Buttons
generate_password_button = Button(text="Generate Password",
                                  command=generate_password)  # Layout width is now governed by the most "E" element
generate_password_button.grid(column=2, row=3, padx=2, pady=2)
add_password_button = Button(text="Add", command=save)  # Used to have width=36
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW", padx=2, pady=2)  # sticky="EW" to center-align & stretch an element
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, columnspan=2, sticky="EW", padx=2, pady=2)

window.mainloop()
