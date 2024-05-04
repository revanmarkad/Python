def func(l, **kwaeg):
    """
    Reverse and title case each string in the list if 'rev_str' is True,
    otherwise, apply title case only.
    
    Args:
        l: List of strings.
        **kwaeg: Keyword arguments.
    
    Returns:
        List of strings with title case applied.
    """
    if kwaeg.get("rev_str") == True:
        # If 'rev_str' is True, reverse each string and apply title case
        return [s[::-1].title() for s in l]
    else:
        # Otherwise, apply title case only
        return [s.title() for s in l]

# List of strings
l = ['revan', 'markad']

# Call the function with the list and the keyword argument rev_str=True
print(func(l, rev_str=True))
