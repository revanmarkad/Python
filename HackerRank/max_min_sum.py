# Question:
# Write two functions to find the minimum and maximum sums of five integers in an array. 
# Each function takes an array of integers as input. The first function, miniMaxSum,
# calculates the minimum and maximum sums by excluding one element at a time and printing the results.
# The second function, minMaxSum, calculates the minimum and maximum sums by subtracting the smallest and largest elements, respectively,
# from the sum of all elements and prints the results.

def miniMaxSum(arr):
    small = arr.index(min(arr))
    big = arr.index(max(arr))
    
    if small == big:
        print(4 * arr[small], 4 * arr[big])
        return
    
    min_sum = max_sum = 0
    
    for i in range(len(arr)):
        if i != small:
            max_sum += arr[i]
        if i != big:
            min_sum += arr[i]
    
    print(min_sum, max_sum)

miniMaxSum([1,2,3,4,5,6])

def minMaxSum(arr):
    small = arr.index(min(arr))
    big = arr.index(max(arr))

    min_sum = sum(arr) - arr[big]
    max_sum = sum(arr) - arr[small]

    print(min_sum, max_sum)
 
minMaxSum([1,2,3,4,5,6])
