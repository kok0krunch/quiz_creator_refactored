import os
from file_quiz import FileQuiz

class QuestionCreator(FileQuiz):
    def __init__(self, output_file="quiz_questions.txt"):
        super().__init__(output_file)
        self.output_file = output_file