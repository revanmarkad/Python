# Create a dictionary using dictionary comprehension
square = {f'Square of {num} is': num**2 for num in range(1, 11)}

# Iterate over the items in the dictionary and print them
for k, v in square.items():
    print(f'{k}: {v}')
