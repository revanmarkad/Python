import datetime

def greet():
    current_time = datetime.datetime.now().time()

    if current_time < datetime.time(12, 0):
        print("Good morning!")
    elif current_time < datetime.time(17, 0):
        print("Good afternoon!")
    else:
        print("Good evening!")

# Call the greet function
greet()
