import random


def get_user_choice():
    user_choice = input("Enter your choice (snake, water, gun): ").lower()
    while user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice. Please enter snake, water, or gun.")
        user_choice = input("Enter your choice (snake, water, gun): ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(["snake", "water", "gun"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "snake" and computer_choice == "water")
        or (user_choice == "water" and computer_choice == "gun")
        or (user_choice == "gun" and computer_choice == "snake")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    print("Welcome to Snake Water Gun Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
