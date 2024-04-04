# Question:
# Given an array of integers, calculate the fractions of its elements that are positive, negative, and zeros.
# Print the decimal value of each fraction with 6 decimal places.

def plusMinus(arr):
    positive = negative = zeros = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeros += 1

    # Calculate the fractions and print them with 6 decimal places
    print("{:.6f}".format(positive/len(arr)))
    print("{:.6f}".format(negative/len(arr)))
    print("{:.6f}".format(zeros/len(arr)))

if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))  # Prompt the user for the number of elements
    arr = []

    # Prompt the user to enter each element and add it to the list
    for _ in range(n):
        element = int(input("Enter an element: "))
        arr.append(element)

    plusMinus(arr)
