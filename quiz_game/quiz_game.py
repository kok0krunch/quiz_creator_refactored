import random
import sys
from colorama import Fore, Style
from file_reader import FileReader

class QuizGame(FileReader):
    def __init__(self, quiz_file="quiz_questions.txt"):
        super().__init__(quiz_file)
        
    def main_menu(self):
        if not self.questions:
            print(Fore.RED + "❌ No questions available. Exiting the quiz." + Style.RESET_ALL)
            sys.exit(1)

        print(Fore.MAGENTA + "🎮 Welcome to the Quiz Game! 🎮" + Style.RESET_ALL)
        print("=" * 50)
        print("1. Start Quiz")
        print("2. Rules of the Quiz")
        print("3. Exit")
        print("=" * 50)
        choice = input(Fore.YELLOW + "👉 Choose an option (1-3): " + Style.RESET_ALL)

        if choice == '1':
            random.shuffle(self.questions)
            correct_answers = 0
            for question_data in self.questions:
                if self.ask_question(question_data):
                    correct_answers += 1
            print(Fore.GREEN + f"\n🎉 You got {correct_answers} out of {len(self.questions)} questions correct! 🎉" + Style.RESET_ALL)
            print(Fore.CYAN + "✨ Thank you for playing! Goodbye! ✨" + Style.RESET_ALL + "\n")
        elif choice == '2':
            self.display_rules()
        elif choice == '3':
            print(Fore.GREEN + "👋 Thank you for visiting the Quiz Game! Goodbye!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Invalid input. Please try again." + Style.RESET_ALL + "\n")
            self.main_menu()