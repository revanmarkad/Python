 
import random

def display_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    user_input = int(input("Your answer (enter the corresponding number): "))
    return user_input - 1  # Adjusting for 0-based index

def kbc_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Paris", "Madrid", "Rome"],
            "correct_answer": 1
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "correct_answer": 1
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_answer": 1
        }
        # Add more questions as needed
    ]

    total_questions = len(questions)
    money_won = 0

    for i in range(total_questions):
        current_question = questions[i]
        user_choice = display_question(current_question["question"], current_question["options"])

        if user_choice == current_question["correct_answer"]:
            print("Correct!\n")
            money_won += 100000  # You can adjust the prize money as needed
        else:
            print("Incorrect! Game Over.")
            break

    print(f"You are taking home ${money_won}!")

if __name__ == "__main__":
    print("Welcome to the KBC Game!\n")
    kbc_game()
