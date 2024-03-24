class Myclass:
    def __init__(self):
        # Initialize instance variables
        self.rNo = 9
        self.name = 'revan'
        
    def display(self):
        # Method to display instance variables
        print(self.rNo)
        print(self.name)      
    
    @staticmethod
    def addition(x, y):
        # Static method to perform addition
        print(x + y)

# Example of using the __init__ method
# Creating an instance of Myclass
# This automatically initializes the instance variables
# No parameters are passed to __init__ because it does not take any
obj = Myclass()

# Example of using the static method
# You call it using the class name itself
Myclass.addition(3, 4)
