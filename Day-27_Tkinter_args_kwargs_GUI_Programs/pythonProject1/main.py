import tkinter
# from tkinter import *  # Imports every class so that you can get rid of "tkinter.Label(), tkinter.Button() and so on

window = tkinter.Tk()  # Creates a Turtle Screen() equivalent
window.title("My First GUI Program")
window.minsize(width=500, height=300)  # Specifies minimum window size however the window will expand with its contents

# Creating components (to be shown on the screen)
# Creating a label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))  # Not enough to show on screen
# my_label.pack()  # Centers and display the component (label) on screen
my_label.pack(side="left")

my_label["text"] = "Any text you want"  # You can access the key word argument in your object and update it like so
my_label.config(text="Another piece of text") # The TKinter specific function can access key word arguments

# Creating a button

button = tkinter.Button








window.mainloop()  # Creates a while loop that listens to input from the user while showing the screen
                   # This always has to be at the end of the program

