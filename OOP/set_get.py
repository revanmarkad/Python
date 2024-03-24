class Employee:
    def SetId(self, id):
        # Method to set the ID of the employee
        self.id = id

    def GetId(self):
        # Method to get the ID of the employee
        return self.id 

    def SetName(self, name):
        self.name = name

    def GetName(self):
        return self.name
        
    def SetSal(self, sal):
        self.sal = sal

    def Getsal(self):
        return self.sal
     
# Creating an instance of the Employee class
m = Employee()

# Setting ID, name, and salary using the respective setter methods
m.SetId(9)
m.SetName("Revan")
m.SetSal(3456789)

# Printing ID, name, and salary using the respective getter methods
print("ID :", m.GetId())
print("NAME :", m.GetName())
print("SALARY :", m.Getsal())
