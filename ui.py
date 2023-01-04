# Import necessary modules
from tkinter import *
from PIL import Image, ImageTk

# Import QuizBrain class from quiz_brain module
from quiz_brain import QuizBrain

# Declare a constant for the theme color of the interface
THEME_COLOR = "#375362"

# QuizInterface class
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Store QuizBrain object and initialize tkinter window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Initialize and grid score label
        self.score_label = Label(text="Score: 0", fg="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Initialize and grid canvas to display question text
        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Initialize and grid true button
        self.true_image = ImageTk.PhotoImage(Image.open("images/true.png"))
        self.true_button = Button(
            image=self.true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        # Initialize and grid false button
        self.false_image = ImageTk.PhotoImage(Image.open("images/false.png"))
        self.false_button = Button(
            image=self.false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        # Get the first question
        self.get_next_question()

        # Start the tkinter main loop
        self.window.mainloop()

    def get_next_question(self):
        # Reset canvas background to white
        self.canvas.config(bg="White")

        # Check if there are still questions left in the quiz
        if self.quiz.still_has_questions():
            # Update score label and get next question
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # Quiz is finished, disable buttons and display end message
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the questions :)"
            )
