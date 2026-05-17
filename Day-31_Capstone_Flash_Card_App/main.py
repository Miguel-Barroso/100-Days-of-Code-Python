from tkinter import *  # Imports all classes and constants, but not free floating modules

import pandas
import random

current_card = {}

#TODO: Note to self, program will crash when running out of cards. Can always check length of the list before commands

try:
    # Try and open an existing saved data file
    with open("data/words_to_learn.csv", "r") as saved_data:
        words_to_learn = pandas.read_csv(saved_data)  # Reads old data and saves into a Python Dict
        data_frame = words_to_learn
except FileNotFoundError:
    # If not found, then the entire language file is used for study
        data_frame = pandas.read_csv("data/french_words.csv")

to_learn = data_frame.to_dict(orient="records")  # Will reformat the data frame into a list of dictionaries
# print(to_learn)  # Each dictionary has two keys (French/English) and the corresponding words
print(type(to_learn))

# Pick out a random card from the pile
def next_card():
    global timer, current_card
    window.after_cancel(timer)
    current_card = random.choice(to_learn)  # Picks a random choice from the list of dictionaries
    print(current_card["French"])
    canvas.itemconfig(card, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    timer = window.after(3000, flip_card)

def known_card():
        with (open("words_to_learn.csv", "w") as saved_data):
            to_learn.remove(current_card)  # Updates the list of words and saves it to words to learn
            data_frame = pandas.DataFrame(to_learn)
            data_frame.to_csv("data/words_to_learn.csv", index=False, header=True)

        next_card()

# Change to backside of card
def flip_card():
    translation = current_card["English"]
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=translation)


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Window width not specified as elements will auto stretch it
timer = window.after(3000, flip_card)

# Canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)  # Removes the thin line
card_front_image = PhotoImage(file="images/card_front.png")  # Used to traverse file systems and get hold of an image
card_back_image = PhotoImage(file="images/card_back.png")  # Imports the backside image must be done outside a func.
card = canvas.create_image(400, 263, image=card_front_image)  # Needs PhotoImage object as input as well as xy positions
canvas.grid(column=0, row=0, columnspan=2)

# Canvas text (text layers that are relative to the canvas)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

# Buttons

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=known_card)
check_button.grid(column=1, row=1)

# Prepare the first card
next_card()

window.mainloop()  # Keeps window up
