def superDigit(n, k):
    # Calculate the super digit of a single number
    def calc_super_digit(num):
        # If num has only one digit, return it
        if len(num) == 1:
            return int(num)
        
        # Calculate the sum of the digits
        digit_sum = sum(int(digit) for digit in num)
        
        # Recursively call calc_super_digit on the sum
        return calc_super_digit(str(digit_sum))
    
    # Concatenate the number n k times
    concatenated_n = n * k
    
    # Calculate the super digit of concatenated_n
    return calc_super_digit(concatenated_n)

print(superDigit("99",2))