# Question:
# Write a function named 'diagonalDifference' that calculates the absolute difference between the sums of the diagonals in a square matrix.
# The function takes a 2D array 'arr' as input, representing the square matrix.
# It iterates through each row of the matrix and calculates the sum of the elements along the primary diagonal (top-left to bottom-right) and the sum of the elements along the secondary diagonal (top-right to bottom-left).
# The function then returns the absolute difference between the sums of the two diagonals.

def diagonalDifference(arr):
    # Initialize variables to store the sums of the diagonals
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    
    # Loop through the rows of the matrix
    for i in range(len(arr)):
        # Add the value of the current element to the sum of the left diagonal
        left_diagonal_sum += arr[i][i]
        # Add the value of the element at the opposite position to the sum of the right diagonal
        right_diagonal_sum += arr[i][len(arr) - 1 - i]
    
    # Calculate the absolute difference between the sums of the diagonals
    diagonal_absolute_difference = abs(left_diagonal_sum - right_diagonal_sum)
    
     
    print (diagonal_absolute_difference)
diagonalDifference([
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
)