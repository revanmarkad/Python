import numpy as np

# Define a 2D NumPy array
my_array = np.array([[11, 22, 3, 4],
                     [5, 67, 7, 8],
                     [95, 10, 11, 12],
                     [13, 14, 15, 16]])

# Print the original array
print("Original array:")
print(my_array)

 
# Convert the array to a matrix
matrices = np.matrix(my_array)
print("Array converted to matrix:")
print(matrices)

 
# Create a matrix directly
mt = np.matrix('1,2,3; 4,3,2; 9,8,7')
print("Directly created matrix:")
print(mt)

 
# Transpose the matrix
'''A transposed matrix is a matrix where the rows of the original matrix become the columns,
 and the columns become the rows. It's obtained by swapping the rows and columns of the original matrix.'''
mt2 = mt.transpose()
print("Transposed matrix:")
print(mt2)

 
# Extract diagonal elements of the array
diagonal = my_array.diagonal()
print("Diagonal elements of the matrix:", diagonal)

 
# Sort the array along rows
print("Row-wise sorting:")
sorting = np.sort(my_array, axis=0)
print(sorting)

 
# Sort the array along columns
print("Column-wise sorting:")
sorting = np.sort(my_array, axis=1)
print(sorting)

 
# Find the maximum element in the array
print("Maximum element in the matrix:")
max_element = np.max(my_array)
print(max_element)

 
# Find the minimum element in the array
print("Minimum element in the matrix:")
min_element = np.min(my_array)
print(min_element)

 
# Compute the square root of each element in the array
print("Square root of elements in the matrix:")
sqrt = np.sqrt(my_array)
print(sqrt)

 
# Compute the sum of all elements in the array
print("Sum of all elements in the matrix:")
sum_elements = np.sum(my_array)
print(sum_elements)
