from tkinter import *
import math
# ---------------------------- macOS Alarm Sounds ------------------------------- #

import subprocess
def play_sound(name="Glass"):
    subprocess.run(["afplay", f"/System/Library/Sounds/{name}.aiff"])

# ---------------------------- Preparing for PyInstaller ------------------------------- #
import os
import sys

# PyInstaller extracts bundled files to a temporary folder at runtime.
# That folder path is stored in sys._MEIPASS.
# When running normally (not bundled), _MEIPASS does not exist,
# so we fall back to the current working directory.
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark_text = ""  # Initializes the string that holds onto check marks
# timer = None  # Initializes the variable that will hold onto the timer object
timer: str | None = None  # This stops PyCharm from warning that time expects a str


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer, check_mark_text
    if timer is not None:
        window.after_cancel(timer)  # Cancels timer only if it exists
        timer = None
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_text = ""  # Reset all check marks
    check_marks.config(text=check_mark_text)  # Update the check mark text field
    reps = 0
    # window.bell()  # Makes a sound when times is reset
    play_sound()

# ---------------------------- TIMER END ------------------------------- #

def end_timer():
    global reps, timer
    reps = 0
    if timer is not None:
        window.after_cancel(timer)  # Cancels timer only if it exists
        timer = None
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="Good Job!")
    # window.bell()  # Makes a sound when times is reset
    play_sound()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    window.attributes('-topmost', True) # To keep the window on top of other windows

    global reps, check_mark_text
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # For testing purposes use these
    # work_sec = 5
    # short_break_sec = 2
    # long_break_sec = 4

    if reps % 2 != 0:
        print(f"Reps = {reps}, Work sec = {work_sec}")
        # If it's the 1st/3rd/5th/7th rep:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        print(f"Reps = {reps}, long break = {long_break_sec}")
        # If it's the 8th rep:
        title_label.config(text="Long Break", fg=RED)
        check_mark_text += "☕"
        check_marks.config(text=check_mark_text)
        count_down(long_break_sec)
    else:
        print(f"Reps = {reps}, short break sec = {short_break_sec}")
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check_mark_text, timer, reps
    # Formatting the timer
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Every sec, call count_down with the updated count
        canvas.itemconfig(timer_text,
                          text=f"{count_min}:{count_sec}")  # Updates a particular canvas object, i.e., timer_text
    elif count == 0:
        canvas.itemconfig(timer_text,
                          text="00:00")  # Updates a particular canvas object, i.e., timer_text
        # window.bell()  # Makes a sound when timer hits 0
        play_sound()
        if reps % 8 == 0:
            end_timer()  # Ends the timer after the long break (4th cycle)
            return  # Stops execution of the rest
        if reps % 2 != 0:
            check_mark_text += "✓"
            check_marks.config(text=check_mark_text)  # Adds check mark after every work cycle
        if reps < 8:
            window.after(1000, start_timer)  # Wait 1 second, then start the next timer unless after long break


    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=5, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)  # Creates a canvas image which handles layers of elements like images and text
tomato_image = PhotoImage(file=resource_path("tomato.png"))  # Used to traverse file systems and get hold of an image
canvas.create_image(100, 112, image=tomato_image)  # Needs PhotoImage object as input as well as x, y canvas positions
timer_text = canvas.create_text(100, 130, text="Ready?", fill="white",
                                font=(FONT_NAME, 35, "bold"))  # Adds text on top of the previous layer on the canvas
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))  # text="✓",
check_marks.grid(column=1, row=2)

window.mainloop()
