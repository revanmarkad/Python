a = input("Enter any value between 1 and 10 :")

if a == "quit":
    print("valid input")

else:
    if int(a) < 1 or int(a) > 10:
        ValueError("invalid input")
