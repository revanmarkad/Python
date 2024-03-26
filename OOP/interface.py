from abc import *

class MyDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    def disconnect(self):
        pass
    
# Concrete subclass representing MySQL database
class MySql(MyDatabase):
    def connect(self):
        print("MySQL connected successfully.......")
        
    def disconnect(self):
        print("MySQL disconnected successfully......")

# Concrete subclass representing Oracle database
class Oracle(MyDatabase):
    def connect(self):
        print("Oracle connected successfully")
        
    def disconnect(self):
        print("Oracle disconnected successfully")
        
# Prompting the user to enter the database name
base_connection = input("Enter Database Name: ")

# Retrieving the class object based on the user's input using globals()
database_name = globals()[base_connection]

# Creating an instance of the selected database class
d1 = database_name()

# Calling the disconnect method
d1.disconnect() #connect
