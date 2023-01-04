import html  # module for unescaping HTML characters

# QuizBrain class
class QuizBrain:
    def __init__(self, q_list):
        # Initialize instance variables
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        # Check if there are still questions left in the list
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get next question in the list and update current question and question number
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Unescape HTML characters in the question text and return formatted string
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        # Check if user's answer is correct and update score accordingly
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
