from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)  # We're passing the quiz questions object for the quiz_ui object to display

# while quiz.still_has_questions():
#     quiz.next_question()  # Cannot have a while loop when running a mainloop such as in Tk()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
