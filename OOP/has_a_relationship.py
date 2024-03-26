# "Has-a" Relationship: This refers to a composition relationship between classes, where one class contains another class as a part of its state. When a class "has-a" relationship with another class, it means that instances of the first class contain instances of the second class as part of their composition.



class Employee:
    # Method to set the ID of the employee
    def SetId(self, id):
        self.id = id

    # Method to get the ID of the employee
    def GetId(self):
        return self.id 

    # Method to set the name of the employee
    def SetName(self, name):
        self.name = name

    # Method to get the name of the employee
    def GetName(self):
        return self.name
        
    # Method to set the salary of the employee
    def SetSal(self, sal):
        self.sal = sal

    # Method to get the salary of the employee
    def Getsal(self):
        return self.sal
     
# Creating an instance of the Employee class
# accessing data members of a class using an object we can say it is like   "has-a" relationship or "object relationship."
m = Employee()

# Setting ID, name, and salary using the respective setter methods
m.SetId(9)
m.SetName("Revan")
m.SetSal(3456789)

# Printing ID, name, and salary using the respective getter methods
print("ID :", m.GetId())
print("NAME :", m.GetName())
print("SALARY :", m.Getsal())
