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
    
    def add_question(self, question, choices, correct_answer):
        with open(self.output_file, "a") as file:
            file.write(f"Question: {question}\n")
            for i, option in enumerate(['a', 'b', 'c', 'd']):
                file.write(f"Option {option}: {choices[i]}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("-" * 50 + "\n")
            self.questions_added += 1
            
    def get_total_questions(self):
        return self.questions_added