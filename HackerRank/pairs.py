    # """
    # Counts the number of pairs in the array with the difference k.
    
    # Args:
    # k (int): The target difference.
    # arr (list of int): The array of integers.
    
    # Returns:
    # int: The number of pairs with the difference k.
    # """

def pairs(k, arr):
    num_set = set(arr)
    count = 0
    
    for num in arr:
        if num + k in num_set:
            count += 1
        if num - k in num_set and k != 0:
            count += 1
    
    return count // 2
