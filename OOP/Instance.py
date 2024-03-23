class MyClass:
    def __init__(self):
        # Initializing instance variables
        self.first_number = 10
        self.second_number = 20
        
    def Test(self):
        # Adding instance variable within a method
        self.third_number = 30
        
# Creating an instance of MyClass
m = MyClass()
# Adding another instance variable directly to the instance
m.additional_number = 90

# Printing the dictionary of instance variables for the first instance
print("Instance variables for m:", m.__dict__)

# Creating another instance of MyClass
m2 = MyClass()

# Printing the dictionary of instance variables for the second instance
print("Instance variables for m2:", m2.__dict__)
