import os

class FileQuiz:
    def __init__(self, output_file="quiz_questions.txt"):
        self.output_file = output_file
        self.questions_added = 0
        # Check if the file exists; if not, write the header
        self._initialize_file()
    
    def _initialize_file(self):
        if not os.path.exists(self.output_file):
            with open(self.output_file, "w") as file:
                file.write("Quiz Questions\n")
                file.write("=" * 50 + "\n")