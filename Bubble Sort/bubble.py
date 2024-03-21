import array as arr

# Initialize an array to store the elements
my_arr = arr.array('i', [])

# Take input for the limit of the array
n = int(input("Enter the limit: "))

# Prompt the user to input elements
print("Enter the elements in the array:")
for i in range(n):
    x = int(input())
    my_arr.append(x)
    
# Bubble sort algorithm
for i in range(n):
    for j in range(n-i-1):
        if my_arr[j] > my_arr[j+1]:
            # Swap elements if they are in the wrong order
            temp = my_arr[j]
            my_arr[j] = my_arr[j+1]
            my_arr[j+1] = temp
            
# Print the sorted array
print("Sorted array:", my_arr)
