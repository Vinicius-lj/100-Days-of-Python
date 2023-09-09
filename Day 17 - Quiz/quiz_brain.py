class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {question.text} (True/False)?")
        self.checck_answer(answer, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def checck_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print("You're right!🎉")
        else:
            print("Incorrect answer.😢")
            print(f"The correct answer was {answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
