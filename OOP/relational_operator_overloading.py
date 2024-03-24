class NumberComparison:
    def __init__(self, value):
        # Initialize instance variable
        self.value = value
    
    def __gt__(self, other):
        # Overload the greater than (>) operator
        # Compare the value of the current object with the value of 'other' object
        if self.value > other.value:
            return True
        else:
            return False

# Create instances of NumberComparison class
number1 = NumberComparison(9)
number2 = NumberComparison(12)

# Compare the instances using the overloaded operator
if number1 > number2:
    print('number1 is greater')
else:
    print("number2 is greater")
