import random
import sys
from colorama import Fore, Style
from file_reader import FileReader

class QuizGame(FileReader):
    def __init__(self, quiz_file="quiz_questions.txt"):
        super().__init__(quiz_file)
        
    def ask_question(self, question_data):
        print(Fore.LIGHTCYAN_EX + "\n❓ " + question_data["question"] + Style.RESET_ALL)
        for key, value in question_data["options"].items():
            print(Fore.WHITE + f"   {key}: {value}" + Style.RESET_ALL)
        user_answer = input(Fore.YELLOW + "👉 Your answer (a, b, c, d): " + Style.RESET_ALL).lower()
        if user_answer == question_data["correct_answer"]:
            print(Fore.GREEN + "🎉 Correct! Great job!" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + f"❌ Wrong! The correct answer was: {question_data['correct_answer']}" + Style.RESET_ALL)
            return False
        
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
    
    def display_rules(self):
        print(Fore.CYAN + "\n📜 Rules of the Quiz:" + Style.RESET_ALL)
        print("1️⃣  Each question has four options: a, b, c, and d.")
        print("2️⃣  Enter the letter corresponding to your answer.")
        print("3️⃣  You will be informed if your answer is correct or wrong.")
        print("4️⃣  Have fun and do your best!")
        main = input(Fore.LIGHTBLUE_EX + "\n" + "👉 Would you like to return to the main menu? (yes/no): " + Style.RESET_ALL).lower()
        if main == 'yes':
            print(Fore.LIGHTGREEN_EX + "🔄 Returning to the main menu..." + Style.RESET_ALL + "\n")
            self.main_menu()
        else:
            print(Fore.RED + "👋 Exiting the quiz. Goodbye!" + Style.RESET_ALL)
            sys.exit(0)