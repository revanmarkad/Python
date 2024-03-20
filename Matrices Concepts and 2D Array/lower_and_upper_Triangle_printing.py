import numpy as np
import array as arr

m, n = [int(a) for a in input("Enter the number of rows and columns: ").split()]


elem = m * n


my_array = arr.array('i', [])


print("Enter %d elements in the matrix:" % elem)


for i in range(elem):
    b = int(input())
    my_array.append(b)

 
my_array2 = np.reshape(my_array, (m, n))
print(my_array2)

# Print the lower triangle of the matrix
print("Lower triangle of the matrix:")
for r in range(m):
    for c in range(n):
        if r >= c:
            print(my_array2[r][c], end=" ")
    print()

# Print the upper triangle of the matrix
print("Upper triangle of the matrix:")
for r in range(m):
    for c in range(n):
        if r <= c:
            print(my_array2[r][c], end=" ")
    print()
