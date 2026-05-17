from tkinter import *


def miles_to_km():
    km = float(user_input.get()) * 1.609
    result_label.config(text=round(km, 1))


window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
# Labels
miles = Label(text="miles")
miles.grid(column=2, row=0)
km = Label(text="KM")
km.grid(column=2, row=1)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
result_label = Label(text="0",)
result_label.grid(column=1, row=1)
# Entry
user_input = Entry(width=10)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)
# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
