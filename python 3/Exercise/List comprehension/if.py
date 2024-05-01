# Create a list containing numbers from 1 to 10
num = list(range(1, 11))

# List comprehension to filter even numbers from 'num' list
# 'i' represents each element in 'num', and the condition 'if i % 2 == 0' checks if the element is even
ans = [i for i in num if i % 2 == 0]

# Print the list containing even numbers
print(ans)

# List comprehension to filter odd numbers from 'num' list
# Similar to the previous comprehension, but this time it checks for odd numbers with the condition 'if i % 2 != 0'
odd_num = [i for i in range(1, 11) if i % 2 != 0]

# Print the list containing odd numbers
print(odd_num)
