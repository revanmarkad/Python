class MyClass:
    def __init__(self, value):
        # Initialize instance variable
        self.value = value

    def __add__(self, other):
        # Overload the addition operator
        # Add the value of 'other' object to the value of current object
        self.value += other.value
        return self.value

    def __sub__(self, other):
        # Overload the subtraction operator
        # Subtract the value of 'other' object from the value of current object
        self.value -= other.value
        return self.value

    def __mul__(self, other):
        # Overload the multiplication operator
        # Multiply the value of 'other' object with the value of current object
        self.value *= other.value
        return self.value

    def __truediv__(self, other):
        # Overload the division operator
        # Divide the value of current object by the value of 'other' object
        self.value /= other.value
        return self.value

    def __floordiv__(self, other):
        # Overload the floor division operator
        # Perform floor division of the value of current object by the value of 'other' object
        self.value //= other.value
        return self.value

    def __mod__(self, other):
        # Overload the modulus operator
        # Compute the modulus of the value of current object with the value of 'other' object
        self.value %= other.value
        return self.value

    def __pow__(self, other):
        # Overload the exponentiation operator
        # Raise the value of current object to the power of 'other' object
        self.value **= other.value
        return self.value
        
# Create instances of MyClass
m = MyClass(40)
m1 = MyClass(10)

# Perform arithmetic operations
addition_result = m + m1
subtraction_result = m - m1
multiplication_result = m * m1
division_result = m / m1
floor_division_result = m // m1
modulus_result = m % m1
exponentiation_result = m ** m1

# Print results
print("Addition result:", addition_result)
print("Subtraction result:", subtraction_result)
print("Multiplication result:", multiplication_result)
print("Division result:", division_result)
print("Floor division result:", floor_division_result)
print("Modulus result:", modulus_result)
print("Exponentiation result:", exponentiation_result)
