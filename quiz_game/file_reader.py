import os
import sys
from colorama import Fore, Style

class FileReader:
    def __init__(self, quiz_file="quiz_questions.txt"):
        self.quiz_file = quiz_file