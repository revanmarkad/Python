# Bill Division

def bonAppetit(bill, k, b):
    total_cost = sum(bill)  # Calculate the total cost of all items
    anna_share = (total_cost - bill[k]) // 2  # Calculate Anna's total share excluding the item she didn't eat
    
    if b > anna_share:  # Check if Anna's contribution is greater than her share
        return b - anna_share  # Return the amount Brian owes Anna if he overcharged her
    else:
        return total_cost // 2 - b  # Calculate and return the refund amount if Anna's share was less than b

 
print(bonAppetit([3, 10, 2, 9],1,12))