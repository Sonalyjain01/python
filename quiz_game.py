import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.question_index = 0
        self.score = 0
        
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        
        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack(pady=20)
        
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(self.window, textvariable=self.answer_var)
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=5)
        
        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack(pady=10)
        
        self.next_question()
        
        
        #self.window.mainloop()
    
    def next_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            self.question_label.configure(text=question["text"])
            self.answer_var.set("")
        else:
            messagebox.showinfo("Quiz Game", f"Quiz completed! Your score is {self.score}/{len(self.questions)}")
            self.window.destroy()
    
    def submit_answer(self):
        answer = self.answer_var.get().strip()
        question = self.questions[self.question_index]
        
        if answer.lower() == question["answer"].lower():
            self.score += 1
        elif answer.lower() != question["answer"].lower():
            self.score -= 0.25
        
        self.question_index += 1
        self.score_label.configure(text=f"Score: {self.score}")
        self.next_question()

# Define the questions for the quiz
questions = [
    {
        "text": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "text": "What is the largest planet in our solar system?",
        "answer": "Jupiter"
    },
    {
        "text": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci"
    },
    {
        "text": "What is the maximum length of a Python identifier?",
        "answer": "No fixed length is specified"
    },
    {
        "text": "What will be the output of the following code snippet? print(2*3 + (5 + 6)*(1 + 1))",
        "answer": "129"
    },
    {
        "text": "Which of the following concepts is not a part of Python?",
        "answer": "pointers"
    },
    {
        "text": "Which of the following types of loops are not supported in Python?",
        "answer": "do-while"
    },
    {
        "text": "What will be the output of the following code snippet?",
        "answer": "Even"
    },
    {
        "text": "If NOIDA is written as OPJEB, then what will be the code for DELHI?",
        "answer": "EFMIJ"
    },
    {
        "text": "If CAT is coded as PATC, JOY is coded as POYJ; similarly the word WING will be coded as",
        "answer": "PINGW"
    },
    {
        "text": " Which number should come next in the series 1, 2, 3, 10, _",
        "answer": "99"
    },
    {
        "text": "Which number is wrong in the series 2, 6, 15, 31, 56, 93?",
        "answer": "93"
    },
    {
        "text": "If PINK is coded as 1691411, then RED will be coded as -",
        "answer": "1854"
    },
    {
        "text": "Which of the following is not an operating system?",
        "answer": "Oracle"
    },
    {
        "text": "When was the first operating system developed?",
        "answer": "1950"
    },
    {
        "text": "Which of the following is the extension of Notepad?",
        "answer": ".txt"
    },
    {
        "text": "When does page fault occur?",
        "answer": "The page does not present in memory."
    },
    {
        "text": "Which is the Linux operating system?",
        "answer": "Open-source operating system"
    },
    {
        "text": "A huge collection of the information or data accumulated form several different sources is known as ________:",
        "answer": "Data Warehouse"
    },
    {
        "text": "Which one of the following refers to the 'data about data'?",
        "answer": "Meta data"
    },
    {
        "text": "To which of the following the term 'DBA' referred?",
        "answer": "Database Administrator"
    },
    {
        "text": "In general, a file is basically a collection of all related______.",
        "answer": "Records"
    },
    {
        "text": "Which of the following refers to the number of tuples in a relation?",
        "answer": "Cardinality"
    },
    {
        "text": "What is the pH value of the human body?",
        "answer": "7.0 to 7.8"
    },
    {
        "text": "Elections to panchayats in state are regulated by",
        "answer": "State Election Commision"
    },
    {
        "text": "Forming of Association in India is",
        "answer": "Fundamental Right"
    },
    {
        "text": "Chelaiya Samiti is related to which of the following?",
        "answer": "Tax reforms"
    },
    {
        "text": "Which of the given cities is located on the bank of river Ganga?",
        "answer": "Patna"
    }
    
    
    
]

# Create an instance of the QuizGame
game = QuizGame(questions)


