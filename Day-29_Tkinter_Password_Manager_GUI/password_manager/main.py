import pyperclip
import random
from tkinter import *  # Imports all classes and constants, but not free floating modules
from tkinter import messagebox  # Module to use system dialogs. NB! Not a class!

delimiter = " | "


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

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    # List comprehensions instead of for loops
    # Appends a random choice from the lists above for a randomized range
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

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
    new_entry = website + delimiter + username + delimiter + password + "\n"
    #  print(new_entry)

    # Data validation
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Data Validation Warning!", message="Don't leave any fields empty!")
    else:
        # Displays the confirmation message
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n"
                                                              f"Website: {website}\n"
                                                              f"Username: {username}\n"
                                                              f"Password: {password}\n\n"
                                                              f"Is it okay to save?")

        # Goes ahead and saves the information if user chooses Yes
        if is_ok:
            file = open("data.text", "a")
            file.write(new_entry)
            file.close()

        # Deletes the contents of the entries on screen
        website_entry.delete(0, END)
        password_entry.delete(0, END)


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
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
username_entry = Entry()  # Used to have width=35
username_entry.insert(END, "miguel@miguelbarroso.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry()  # Used to have width=21
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password",
                                  command=generate_password)  # Layout width is now governed by the most "E" element
generate_password_button.grid(column=2, row=3)
add_password_button = Button(text="Add", command=save)  # Used to have width=36
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")  # sticky="EW" to center-align & stretch an element

window.mainloop()
