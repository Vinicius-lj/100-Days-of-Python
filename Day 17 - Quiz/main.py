from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank += [
        Question(question["text"], question["answer"])
    ]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulation! You've finished the Quiz.")
print(f"You're final score was {quiz.score}/{quiz.question_number}")
