# import tkinter  # Imports the module but you have to specify which Class you are gonna use
from tkinter import *  # Imports every class so that you can get rid of "tkinter.Label(), tkinter.Button() and so on

def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)

window = Tk()  # Creates a Turtle Screen() equivalent
window.title("My First GUI Program")
window.minsize(width=500, height=300)  # Specifies minimum window size however the window will expand with its contents
window.config(padx=20, pady=20)  # Adds padding to the margins of the window

# Creating components (to be shown on the screen)

# Creating a label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))  # This is not enough to show on screen therefore
# my_label.pack()                                                  # my_label.pack() is used to centers and display the
# my_label.place(x=0, y=0)                                         # component (label) on screen
my_label.grid(column=0, row=0)

my_label["text"] = "Any text you want"         # You can access the key word argument in your object and update
my_label.config(text="Another piece of text")  # This Tkinter specific function can access key word arguments

# Creating a button
button = Button(text="Click Me", command=button_clicked)  # command keyword is basically an event listener
# button.pack()                                           # that will call the specified function
button.grid(column=1, row=1)

# Creating an Entry (input)

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# New button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
# new_button.config(padx=20, pady=20)  # Adds padding to the specified widget





window.mainloop()  # Creates a while loop that listens to input from the user while showing the screen
                   # This always has to be at the end of the program

