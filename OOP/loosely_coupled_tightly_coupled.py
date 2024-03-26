# Program for Loosely and Tightly Coupled Application

# Importing the Abstract Base Class module
from abc import *

# Interface Definition: Database (Abstract class)
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

# Concrete Implementation: Oracle (Inherits from Database)
class Oracle(Database):
    def connect(self):
        print("Oracle Connection Success")
    
    def disconnect(self):
        pass

# Concrete Implementation: Mysql (Inherits from Database)
class Mysql(Database):
    def connect(self):
        print("MYSQL Connection Success")
    
    def disconnect(self):
        print("MYSQL Connection closed")

# Concrete Implementation: Sybase (Inherits from Database)
class Sybase(Database):
    def connect(self):
        print("SYBASE Connection Success")
    
    def disconnect(self):
        print("SYBASE Connection closed")

# User Input for Database Name
dname = input("Enter Database Name: ")

# Dynamic Class Instantiation based on User Input
cname = globals()[dname]
D1 = cname()
D1.connect()

# Performing Database Operations
print("Database Insert")
print("Database Search")
print("Database Delete")
print("Database Update")

# Disconnecting from the Database
D1.disconnect()