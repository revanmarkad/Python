def findZigZagSequence(a, n):
    """
    This function takes a list of integers 'a' and its length 'n' as input
    and prints the zigzag sequence of the sorted list.

    Parameters:
        a (list): List of integers.
        n (int): Length of the list 'a'.

    Returns:
        None
    """
    # Sort the list 'a'
    a.sort()

    # Find the middle index
    mid = int((n + 1) / 2) - 1

    # Swap the middle element with the last element
    a[mid], a[n - 1] = a[n - 1], a[mid]

    # Initialize start and end indices for zigzag pattern
    st = mid + 1
    ed = n - 2

    # Swap elements in zigzag pattern
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1

    # Print the zigzag sequence
    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')


# Example usage
findZigZagSequence([1, 2, 3, 4, 5, 8, 9], 7)
