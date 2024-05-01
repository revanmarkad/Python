lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to create a new list based on elements of 'lst'
# For even numbers, multiply by 2; for odd numbers, multiply by -1
new = [i * 2 if i % 2 == 0 else -i for i in lst]
 
print(new)
