# Question:
# Define a function named 'find' that takes a list 'a' as input. 
# The function should iterate through the elements of the list and print the elements that occur only once.
 

def find(a):
   
    for i in a:
        
        if a.count(i) == 1:
           
            print(i)
            
    # Alternative approach using list comprehension (commented out)
    
    # unique_elements = [x for x in a if a.count(x) == 1]
    # print(unique_elements)
      

find([1, 2, 3, 4, 1, 2, 3])
