from Quiz_game_question_data import question_data
from Quiz_gamequestion_model import Question
from Quiz_game_quiz_brain import Quiz_brain

question_bank = []

for questions in question_data:
    question_bank.append(Question(questions["question"], questions["correct_answer"]))

quiz = Quiz_brain(question_bank)
while quiz.still_has_Question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
