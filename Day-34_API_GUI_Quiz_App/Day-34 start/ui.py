from tkinter import *
from quiz_brain import QuizBrain  # Importing the QuizBrain class

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_SIZE = 20
FONT_STYLE = "italic"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # Here, the datatype is specified as a QuizBrain object
        self.quiz = quiz_brain

        self.window = Tk()  # Creates a new window object from the Tk() class
        self.window.title("Quizzler")  # Sets the title attribute of the window object
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)  # Sets the background color of the window object

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=(FONT_NAME, 14, "normal"), fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,  # By setting width, you can make text wrapping happen
                                                     text="Question text goes here!",
                                                     font=(FONT_NAME, FONT_SIZE, FONT_STYLE),
                                                     fill=THEME_COLOR
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        check_image = PhotoImage(file='images/true.png')  # Notice how 'self' is not used
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.answered_true)  # Image size does not need to be specified
        self.check_button.grid(column=0, row=2)

        cross_image = PhotoImage(file='images/false.png')  # 'self' allows a variable to be accessed elsewhere (no need)
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.answered_false)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()  # Gets the first question when window is loaded

        self.window.mainloop()  # Holds the window in place, nothing after this loop is executed until window is closed

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()  # Calls the method of the QuizBrain class to return a question text
            self.canvas.itemconfig(self.question_text, text=q_text)  # Grabs the question_text canvas object and updates it
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\n"
                                                            f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def answered_true(self):
        answered_correctly = self.quiz.check_answer("True")
        self.give_feedback(answered_correctly)

    def answered_false(self):
        answered_correctly = self.quiz.check_answer("False")
        self.give_feedback(answered_correctly)

    def give_feedback(self, answered_correctly):
        if answered_correctly:
            print("Answered correctly")
            self.canvas.config(bg="green")
        else:
            print("Incorrect")
            self.canvas.config(bg="red")

        # Schedule the canvas color reset and next question after 3 seconds
        self.window.after(1000, self.get_next_question)
