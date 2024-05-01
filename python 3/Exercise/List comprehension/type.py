def check(lst):
    # List comprehension to iterate over elements in 'lst'
    # and convert integers and floats to strings
    # while skipping any elements that are not integers or floats
    return [str(i) for i in lst if type(i) == int or type(i) == float]

 
print(check([True, False, 1, 10, 1.11, 12.33, '99']))
