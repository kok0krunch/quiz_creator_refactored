import os
import sys
from colorama import Fore, Style

class FileReader:
    def __init__(self, quiz_file="quiz_questions.txt"):
        self.quiz_file = quiz_file
        self.questions = self.load_quiz_questions()

    def load_quiz_questions(self):
        if not os.path.exists(self.quiz_file):
            print(Fore.RED + f"❌ Error: The file {self.quiz_file} does not exist." + Style.RESET_ALL)
            sys.exit(1)
        
        with open(self.quiz_file, 'r') as file:
            lines = file.readlines()

        question = None
        options = {}
        correct_answer = None
        questions = []

        for line in lines:
            line = line.strip()
            if line.startswith("Question:"):
                question = line.split("Question:")[1].strip()
            elif line.startswith("Option"):
                option_key, option_value = line.split(":")
                options[option_key.split()[1].strip()] = option_value.strip()
            elif line.startswith("Correct Answer:"):
                correct_answer = line.split("Correct Answer:")[1].strip()
            elif line.startswith("-" * 50):
                if question and options and correct_answer:
                    questions.append({
                        "question": question,
                        "options": options,
                        "correct_answer": correct_answer
                    })
                question = None
                options = {}
                correct_answer = None
        return questions