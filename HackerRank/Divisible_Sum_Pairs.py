 

def divisibleSumPairs(n, k, ar):
    # Initialize a variable to store the count of pairs
    count = 0
    
    # Iterate through the array indices
    for i in range(n):
        for j in range(i + 1, n):  # Start from i + 1 to avoid duplicates
            # Check if the sum of the pair is divisible by k
            if (ar[i] + ar[j]) % k == 0:
                # If condition is met, increment the count
                count += 1
                
    # Return the total count of pairs
    return count

print(divisibleSumPairs(5,5,[1,2,3,4,5,6]))