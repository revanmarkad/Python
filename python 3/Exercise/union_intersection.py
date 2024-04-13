# Define two sets
a = {1, 2, 3, 4, 5, 6}
b = {3, 4, 5, 6, 7, 8, 9, 10}

# Perform union operation
union = a | b  # This combines all unique elements from both sets
print(union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Perform intersection operation
intersection = a & b  # This finds common elements between both sets
print(intersection)  # Output: {3, 4, 5, 6}
