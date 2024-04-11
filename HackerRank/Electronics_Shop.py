import os
import sys

# Function to calculate the maximum amount of money that can be spent on a keyboard and USB drive
def getMoneySpent(keyboards, drives, b):
     
    max_spent = -1  
    
    
    for keyboard_price in keyboards:
         
        for drive_price in drives:
            # Calculate the total cost of buying the current keyboard and USB drive
            total_cost = keyboard_price + drive_price
            # If the total cost is within budget and greater than the maximum spent so far, update max_spent
            if total_cost <= b and total_cost > max_spent:
                max_spent = total_cost
    
    return max_spent

print(getMoneySpent(keyboards = [4, 5, 6], drives = [20, 30, 40], b =70))
 