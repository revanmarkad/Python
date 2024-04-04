# Question:
# Write a function to find the median of a list of integers. 
# The function should return the median value, which is the middle element of the sorted list.
# If the number of elements is odd, return the middle element.
# If the number of elements is even, return the average of the two middle elements.

def findMedian(arr):
    sorted_arr = sorted(arr)  # Sort the array in non-decreasing order
    n = len(sorted_arr)
    if n % 2 == 1:  # If the number of elements is odd
        return sorted_arr[n // 2]  # Return the middle element
    else:  # If the number of elements is even
        mid_left = sorted_arr[n // 2 - 1]
        mid_right = sorted_arr[n // 2]
        return (mid_left + mid_right) // 2  # Return the average of the two middle elements

# Example usage:
print(findMedian([1, 2, 7, 6]))
