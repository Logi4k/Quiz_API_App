# Import necessary classes and data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a list of Question objects from question data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create QuizBrain and QuizInterface objects
quiz = QuizBrain(question_bank)
quiz_gui = QuizInterface(quiz)

# Display final score after quiz is completed
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
