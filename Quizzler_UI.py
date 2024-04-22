from tkinter import *
from Quizzler_quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler-App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(
            text=f"Score: ", font=("Arial", 16), background=THEME_COLOR, fg="white"
        )
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=270,
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
        )

        check_mark = PhotoImage(file="Quizzler_images/true.png")
        self.check_button = Button(
            image=check_mark, highlightthickness=0, command=self.check_is_clicked
        )
        self.check_button.grid(row=2, column=0, padx=20, pady=20)

        cross_mark = PhotoImage(file="Quizzler_images/false.png")
        self.cross_button = Button(
            image=cross_mark, highlightthickness=0, command=self.cross_is_clicked
        )
        self.cross_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check_is_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def cross_is_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#8DECB4")
        else:
            self.canvas.config(bg="#D80032")
        self.window.after(1000, self.get_next_question)
