# Initialize an empty dictionary to store user information
user = {}

# Get user input for name, age, favorite movies, and favorite songs
name = input("What is your name? ")
age = input("What is your age? ")
movies = input("What are your favorite movies? (Enter separated by comma): ").split(",")
songs = input("What are your favorite songs? (Enter separated by comma): ").split(",")

# Add user information to the dictionary
user["name"] = name
user["age"] = age
user["movies"] = movies
user["songs"] = songs

# Print user information with improved formatting
print("User Information:")
for key, value in user.items():
    print(f"{key.capitalize()}: {value}")  # Capitalize the key for better readability
