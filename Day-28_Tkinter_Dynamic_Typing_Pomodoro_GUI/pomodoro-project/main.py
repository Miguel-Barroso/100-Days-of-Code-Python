from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5  # 25
SHORT_BREAK_MIN = 0.5  # 5
LONG_BREAK_MIN = 0.5  # 20
reps = 0
check_mark_text = ""  # Initializes the string that holds onto check marks
timer = None  # Initializes the variable that will hold onto the timer object


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)  # To make the window stay on top of other windows

    global reps
    reps += 1
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60
    # For testing purposes
    work_sec = 25
    short_break_sec = 5
    long_break_sec = 20

    if reps % 2 != 0:
        print(f"Reps = {reps}, Work sec = {work_sec}")
        # If it's the 1st/3rd/5th/7th rep:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        print(f"Reps = {reps}, long break = {long_break_sec}")
        # If it's the 8th rep:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        print(f"Reps = {reps}, short break sec = {short_break_sec}")
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check_mark_text
    global timer
    # Formatting the timer
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Grabs a particular canvas object, i.e., timer_text
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Every sec, call count_down method with the updated count
    elif count == 0:
        start_timer()
        if reps % 2 == 0:
            check_mark_text += "✓"
            check_marks.config(text=check_mark_text)
            window.bell()  # Makes a sound when timer hits 0

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# def print_something(thing):
#     print(thing)
#
# window.after(1000, print_something, "Hello World!")  # Waits 1000 ms, then calls the function and passes the arguments

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)  # Creates a canvas image which handles layers of elements like images and text
tomato_image = PhotoImage(file="tomato.png")  # Used to traverse file systems and get hold of an image
canvas.create_image(100, 112, image=tomato_image)  # Needs PhotoImage object as input as well as x, y canvas positions
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))  # Adds text on top of the previous layer on the canvas
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))  # text="✓",
check_marks.grid(column=1, row=3)

window.mainloop()
