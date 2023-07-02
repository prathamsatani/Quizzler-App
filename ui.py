from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title(string='Quizzler App')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Ariel', 13))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some Question Text', fill=THEME_COLOR, width=280,
                                                     font=('Ariel', 15))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        self.right_button = Button()
        right_image = PhotoImage(file='images/true.png')
        self.right_button.config(image=right_image, command=self.right)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button()
        wrong_image = PhotoImage(file='images/false.png')
        self.wrong_button.config(image=wrong_image, command=self.wrong)
        self.wrong_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text='You reached the end of the quiz')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def right(self):
        answer = 'true'
        retval = self.quiz.check_answer(answer)
        self.give_feedback(retval)

    def wrong(self):
        answer = 'false'
        retval = self.quiz.check_answer(answer)
        self.give_feedback(retval)

    def give_feedback(self, retval):
        if retval:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.next_question)
