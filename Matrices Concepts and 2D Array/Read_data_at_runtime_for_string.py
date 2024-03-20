import numpy as np

# Get the dimensions of the matrix from the user
m, n = [int(a) for a in input("Enter the number of rows and columns: ").split()]
elem = m * n

# Get the elements of the matrix as a single string input
input_str = input('Enter %d elements in the matrix separated by spaces: ' % elem)

# Split the input string into individual elements
elements = input_str.split()

# Convert the elements to a NumPy array and reshape it to the specified dimensions
mt = np.array(elements).reshape((m, n))

print("Matrix:")
print(mt)
