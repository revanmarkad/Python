def minimumBribes(q):
    bribes = 0  # Initialize the number of bribes
    
    n = len(q)  # Get the length of the queue
    
    # Iterate through the queue from right to left
    for i in range(n - 1, -1, -1):
        # Check if the person has moved more than 2 positions ahead
        if q[i] - (i + 1) > 2:
            print("Too chaotic")  # Print "Too chaotic" and exit if so
            return
        
        # Count the number of bribes each person has made
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1  # Increment the bribes count
    
    print(bribes)  # Print the total number of bribes

 