class Test():
    def __init__(self):
        # Initializing instance variables
        self.name = 'revan'
        self.r_num = 9
        self.clg = "GH Raisoni"
        
    def display(self):
        # Displaying instance variables
        print("Name:", self.name)
        print("Roll Number:", self.r_num)
        print("College Name:", self.clg)
    
    def __str__(self):
        # Customizing string representation
        return "Name: {} Roll Number: {} College Name: {}".format(self.name, self.r_num, self.clg)

# Creating an instance of Test class
T = Test()
# Printing the string representation of the instance
print(T)
