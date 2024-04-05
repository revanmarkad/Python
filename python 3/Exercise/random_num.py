import random

random_num = random.randint(1, 5)

user_input = int(input("Enter Number: "))

if user_input == random_num:
    print("Your guess is correct!")
elif user_input > random_num:
    print("Oops! Your guess is too large.")
else:
    print("Oops! Your guess is too small.")
