from tkinter import Tk

def check_timer_type():
    timer_id = window.after(1000, check_timer_type)
    print(f"Type of timer_id: {type(timer_id)}, Value: {timer_id}")

window = Tk()
check_timer_type()
window.mainloop()
