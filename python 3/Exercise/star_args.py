# Define the add function
# with the help of args we can passnore than one argument
def add(*args):
    total = 0
    # Iterate over the arguments and sum them up
    for i in args:
        total += i
    return total

# Test the add function with multiple arguments
print(add(1, 2, 3, 4, 5))  # Output: 15
