import random
import sys
from colorama import Fore, Style
from file_reader import FileReader

class QuizGame(FileReader):
    def __init__(self, quiz_file="quiz_questions.txt"):
        super().__init__(quiz_file)