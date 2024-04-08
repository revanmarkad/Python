import random

ans = random.randint(1, 10)
count = 0

for _ in range(1,11):
    user_input = int(input("Enter a number between 1 and 10: "))

    count += 1
    if user_input == ans:
        print(f"Congratulations! You guessed the correct number {ans} in {count} attempt(s).")
        break
    elif user_input > ans:
        print("Your guess is greater than the correct number.")
    else:
        print("Your guess is smaller than the correct number.")
