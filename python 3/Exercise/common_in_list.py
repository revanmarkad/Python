def common(l1, l2):
    # Initialize an empty list to store common elements
    comm = []
    # Get the minimum length of the two lists
    min_len = min(len(l1), len(l2))

    # Iterate over the indices up to the minimum length
    for i in range(min_len):
        # Check if the element from l1 exists in l2
        if l1[i] in l2:
            # If it does, append it to the common list
            comm.append(l1[i])

    return comm    

# Test the function with sample input
print(common([1, 2, 3, 4], [1, 4, 3, 2]))  # Output: [1, 2, 3, 4]


# Another way to find common elements
def common(l1, l2):
 
    comm = []
  
    for i in range(len(l1)):
        # Iterate over each element of l2
        for j in range(len(l2)):
          
            if l1[i] == l2[j]:
                comm.append(l1[i])
    return comm    

 
print(common([1, 2, 3, 4], [1, 4, 3, 2]))  # Output: [1, 2, 3, 4]
