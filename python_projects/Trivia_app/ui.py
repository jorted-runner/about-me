from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.question_num = 0

        self.window = Tk()
        self.window.title("The Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.question_card = Canvas(height=250, width=300)
        self.question_text = self.question_card.create_text(150,
                                                            125,
                                                            width=280,
                                                            text="Some Question Text",
                                                            font=("Arial", 20, "italic"))
        self.question_card.grid(column=0, columnspan=2, row=1, pady=20)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.correct_button = Button(image=true_img, background=THEME_COLOR, highlightthickness=0,
                                     command=self.answer_true)
        self.correct_button.grid(column=0, row=2, padx=20, pady=20)

        self.false_button = Button(image=false_img, background=THEME_COLOR, highlightthickness=0,
                                   command=self.answer_false)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_card.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_card.config(background="white")
            self.question_card.itemconfig(self.question_text, text=q_text)
        else:
            self.question_card.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        user_answer = "true"
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def answer_false(self):
        user_answer = "false"
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_card.config(bg="green")
        else:
            self.question_card.config(bg="red")
        self.window.after(1000, self.get_next_question)

