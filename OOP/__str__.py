class myclass:
    def __init__(self, id, name, salary):
        # Initializing instance variables
        self.id = id
        self.name = name
        self.salary = salary
    
    def __str__(self):
        # Customizing string representation
        s = 'ID: {} NAME: {} SALARY: {}'.format(self.id, self.name, self.salary)
        return s

# Creating an instance of myclass
m = myclass(9, 'revan', 90000000)
print(m)