def multi(*args):
    """
    Calculate the product of all arguments.
    
    Args:
        *args: Any number of arguments.
    
    Returns:
        The product of all arguments.
    """
    ans = 1
    for i in args:
        ans *= i
    return ans

# Test the function with multiple arguments directly
print("Product of 1, 2, 3, 4:", multi(1, 2, 3, 4))

# Test the function with a list of arguments
lst = [1, 2, 3, 4]
print("Product of elements in list:", multi(*lst))
