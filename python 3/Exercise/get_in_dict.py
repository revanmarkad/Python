# Define a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using the get method
name = my_dict.get('name')
print("Name:", name)  # Output: Name: Alice

# Trying to access a key that doesn't exist
gender = my_dict.get('gender')
print("Gender:", gender)  # Output: Gender: None

# Specifying a default value
job = my_dict.get('job', 'Unemployed')
print("Job:", job)  # Output: Job: Unemployed
