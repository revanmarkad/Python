# Creating a dictionary for 10 students
students = {
    1: {"name": "Alice", "course": "MCA", "admission": "regular", "job": False},
    2: {"name": "Bob", "course": "MCA", "admission": "regular", "job": True},
    3: {"name": "Charlie", "course": "MCA", "admission": "regular", "job": False},
    4: {"name": "David", "course": "MCA", "admission": "regular", "job": True},
    5: {"name": "Eve", "course": "MCA", "admission": "regular", "job": False},
    6: {"name": "Frank", "course": "MCA", "admission": "regular", "job": True},
    7: {"name": "Grace", "course": "MCA", "admission": "regular", "job": False},
    8: {"name": "Helen", "course": "MCA", "admission": "regular", "job": True},
    9: {"name": "Ivy", "course": "MCA", "admission": "regular", "job": False},
    10: {"name": "Jack", "course": "MCA", "admission": "regular", "job": True}
}

# Printing the initial student dictionary
print("Initial Student Dictionary:")
print(students)

# Updating student dictionary to add 4 more students
students.update({
    11: {"name": "Kate", "course": "MCA", "admission": "regular", "job": True},
    12: {"name": "Liam", "course": "MCA", "admission": "regular", "job": False},
    13: {"name": "Mia", "course": "MCA", "admission": "regular", "job": True},
    14: {"name": "Noah", "course": "MCA", "admission": "regular", "job": False}
})

# Printing the updated student dictionary
print("\nUpdated Student Dictionary:")
print(students)
