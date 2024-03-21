import array as arr
import numpy as np

# Take input for the limit of the array
n = int(input("Enter the limit: "))

# Initialize an array to store the elements
myArr = arr.array("i", [])

# Prompt the user to input elements
print("Enter elements:")
for i in range(n):
    x = int(input())
    myArr.append(x)

# Take input for the number to search for
s = int(input("Enter a number for searching: "))

# Reshape and sort the array using NumPy
myArr2 = np.reshape(myArr, (n))
myArr2.sort()

# Initialize variables for binary search
low = 0
high = n - 1
f = 0

# Binary search algorithm
while low <= high:
    mid = (low + high) // 2
    if s == myArr2[mid]:
        f = 1
        break
    elif s > myArr2[mid]:
        low = mid + 1
    else:
        high = mid - 1

# Check if search was successful and print result
if f == 1:
    print("Search successful.")
else:
    print("Search unsuccessful.")
