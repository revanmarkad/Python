def args(num, *args):
    """
    Calculate the power of each argument.
    
    Args:
        num: Exponent to raise each argument to.
        *args: Any number of arguments.
    
    Returns:
        A list containing the result of raising each argument to the power of num,
        or the string 'Args is Empty' if no arguments are provided.
    """
    if args:
        # If arguments are provided, calculate the power of each argument
        return [i**num for i in args]
    else:
        # If no arguments are provided, return a message indicating that args is empty
        return 'Args is Empty'

lst = [1, 2, 3, 4, 5]
print(args(3, *lst))  # Output: [1, 8, 27, 64, 125]
