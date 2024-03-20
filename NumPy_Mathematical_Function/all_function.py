import numpy as np
 
My_Array = np.array([-1, 2, 2, 4, 6, 2, 2])

# Compute the square root of each element in the array
New_Array = np.sqrt(My_Array)
print("Square root of each array element:", New_Array)

# Compute the cube of each element in the array
pwr = np.power(My_Array, 3)
print("Cube of each array element:", pwr)

# Compute the sum of all elements in the array
s_um = np.sum(My_Array)
print("Sum of all array elements:", s_um)

# Compute the product of all elements in the array
product = np.prod(My_Array)
print("Product of all array elements:", product)

# Find the maximum element in the array and its position
max_num = np.max(My_Array)
position = np.argmax(My_Array)
print("Maximum number in array:", max_num)
print("Position of maximum number in array:", position)

# Find the minimum element in the array and its position
min_num = np.min(My_Array)
position1 = np.argmin(My_Array)
print("Minimum number in array:", min_num)
print("Position of minimum number in array:", position1)

# Find the unique elements in the array
unique = np.unique(My_Array)
print("Unique elements of the array:", unique)

# Compute the absolute value of each element in the array
positive = np.abs(My_Array)
print("Absolute values of array elements:", positive)

# Sort the elements of the array in ascending order
sorting = np.sort(My_Array)
print("Sorted array:", sorting)
