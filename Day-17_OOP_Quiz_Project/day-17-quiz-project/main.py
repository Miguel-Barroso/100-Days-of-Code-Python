from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    text = item["question"]
    answer = item["correct_answer"]
    question_object = Question(text, answer)
    question_bank.append(question_object)

# print(question_bank)
# print(question_bank[0].answer)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():  # If there are questions remaining
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
