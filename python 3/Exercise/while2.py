# "Write a Python program that prompts the user to enter a sequence of numbers. Calculate and print the sum of all the digits in the sequence."

n = input("Enter a Numbers :") 
 
total = 0
i=0
while i < len(n):
    total += int(n[i])
    
    i+=1
print("Total is:", total)
