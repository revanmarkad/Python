import numpy as np
import array as arr

# Prompt the user to enter the number of rows and columns
m, n = [int(a) for a in input("Enter the number of rows and columns: ").split()]

# Create an empty array to store the elements
my_Array = arr.array('i', [])

# Calculate the total number of elements in the matrix
elem = m * n

# Prompt the user to enter the elements of the matrix
print('Enter %d elements in the matrix (after entering each number, press Enter):' % elem)

# Iterate over the total number of elements
for i in range(elem):
    # Prompt the user to input each element
    a = int(input())
    # Append the element to the array
    my_Array.append(a)

# Reshape the array to create a 2D NumPy array
my_Array2 = np.reshape(my_Array, (m, n))

# Convert the 2D NumPy array to a matrix
matrix = np.matrix(my_Array2)

# Print the resulting matrix
print("Matrix:")
print(matrix)
