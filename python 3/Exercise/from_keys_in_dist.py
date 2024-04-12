# Using fromkeys() with a list
keys_list = ['name', 'age', 'city']
default_value = 'Unknown'
my_dict = dict.fromkeys(keys_list, default_value)
print(my_dict)
# Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# Using fromkeys() with a tuple
keys_tuple = ('name', 'age', 'city')
my_dict = dict.fromkeys(keys_tuple)
print(my_dict)
# Output: {'name': None, 'age': None, 'city': None}

# Using fromkeys() with a string
keys_string = 'abcde'
default_value = 0
my_dict = dict.fromkeys(keys_string, default_value)
print(my_dict)
# Output: {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
