class Student:
    '''college variable is declared as static in the Student class 
    because it represents a property shared among all instances of the class'''
    
    # Class variable for college name
    college = "GH Raisoni"
    
    def __init__(self, name, roll):
        # Initialize instance variables
        self.name = name
        self.roll = roll
    
    def display(self):
        # Method to display student details
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)
        print("College:", Student.college)
        print()

# Create instances of Student class with meaningful names
student1 = Student("REVAN", 9)
student2 = Student("Sachin", 1)
student3 = Student("Sai", 10)
student4 = Student("Anurag", 7)
student5 = Student("Aniket (Chindra)", 15)

# Display details of each student
student1.display()
student2.display()
student3.display()
student4.display()
student5.display()
