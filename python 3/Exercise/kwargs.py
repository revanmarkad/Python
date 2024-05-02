def func(**kwargs):
    """
    Print key-value pairs of keyword arguments.
    
    Args:
        **kwargs: Any number of keyword arguments.
    """
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# Call the function with keyword arguments
func(f_name="Revan", l_name='Markad')
