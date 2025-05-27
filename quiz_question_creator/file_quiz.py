import os

class FileQuiz:
    def __init__(self, output_file="quiz_questions.txt"):
        self.output_file = output_file
        self.questions_added = 0