def libraryFine(d1, m1, y1, d2, m2, y2):
 
    total = 0  # Initialize the fine amount to zero
    
    # Check if the return year is greater than the due year
    if y1 > y2:
        total += 10000  # Add 10000 to the total fine
        
    # If the return year is the same as the due year, check the months
    elif y1 == y2 and m1 > m2:
        total += 500 * (m1 - m2)  # Add 500 times the number of months late to the total fine
        
    # If both the year and month are the same, check the days
    elif y1 == y2 and m1 == m2 and d1 > d2:
        total += 15 * (d1 - d2)  # Add 15 times the number of days late to the total fine
        
    return total  
