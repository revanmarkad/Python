# Using dictionary comprehension
def cube(n):
    # Generate a dictionary using a dictionary comprehension
    # Key: number from 1 to n
    # Value: cube of the key
    return {i: i**3 for i in range(1, n+1)}

 
print(cube(50))


# Using a for loop
def cube(n):
    cubes = {}  # Initialize an empty dictionary to store cubes
    
    # Iterate over numbers from 1 to n
    for i in range(1, n+1):
        key = i      # Current number is the key
        value = i**3  # Cube of the current number is the value
        cubes[key] = value  # Add key-value pair to the dictionary
    
     
    return cubes 

 
print(cube(50))
