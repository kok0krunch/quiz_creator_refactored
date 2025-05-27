import os
from file_quiz import FileQuiz

class QuestionCreator(FileQuiz):
    def __init__(self, output_file="quiz_questions.txt"):
        super().__init__(output_file)
        self.output_file = output_file
        
    def create_quiz(self):
        print("=" * 50)
        print("🎉 Welcome to the Quiz Question Creator! 🎉")
        print("=" * 50)

        while True:
            print("\nLet's create a new quiz question!")
            question = input("📝 Enter the question: ").title()

            choices = []
            print("\n💡 Enter options for answers (a, b, c, d):")
            for option in ['a', 'b', 'c', 'd']:
                choice = input(f"   ➡ Option {option}: ").title()
                choices.append(choice)

            correct_answer = input("\n✅ Enter the correct answer (a, b, c, d): ").lower()
            while correct_answer not in ['a', 'b', 'c', 'd']:
                print("❌ Invalid option. Please enter a, b, c, or d.")
                correct_answer = input("✅ Enter the correct answer (a, b, c, d): ").lower()

            # Add the question to the quiz
            self.add_question(question, choices, correct_answer)
            print(f"\n🎉 Question added successfully!")

            # Ask if the user wants to add another question
            another_question = input("\n➕ Do you want to add another question? (yes/no): ").lower()
            if another_question != 'yes':
                print("\n✨ Thank you for using the Quiz Question Creator!")
                print(f"📂 Quiz data saved to: {os.path.abspath(self.output_file)}")
                print(f"📊 Total questions added: {self.get_total_questions()}")
                break