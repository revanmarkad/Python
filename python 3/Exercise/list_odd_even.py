# Function to separate odd and even numbers into two separate lists
def odd_even(ls):
     
    new_ls = [["EVEN :"], ["ODD :"]]
    
    # Iterate through the input list
    for num in ls:
        
        if num % 2 == 0:
            
            new_ls[0].append(num)
        else:
             
            new_ls[1].append(num)
    
     
    return new_ls

 
print(odd_even([1, 2, 3, 4, 5, 6, 7]))

# Another way to achieve the same result using list comprehensions
def odd_even(ls):
    # Create lists of even and odd numbers using list comprehensions
    even = ["EVEN :"] + [num for num in ls if num % 2 == 0]
    odd = ["ODD :"] + [num for num in ls if num % 2 != 0]
    
   
    return [even, odd]
 
print(odd_even([1, 2, 3, 4, 5, 6, 7]))
