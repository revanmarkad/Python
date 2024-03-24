" How Many Ways We Can Use Static Variables"

class MyClass:
    # Static variable
    total_value = 100
    
    def __init__(self):
        # Increment static variable in constructor
        MyClass.total_value += 10
        
    def increment_by_non_static_method(self):
        # Increment static variable by a non-static method
        MyClass.total_value += 10
        
    @staticmethod
    def increment_by_static_method():
        # Increment static variable by a static method
        MyClass.total_value += 10
        
    @classmethod
    def increment_by_class_method(cls):
        # Increment static variable by a class method
        cls.total_value += 10
        
        
# Create an instance of MyClass
t1 = MyClass()

# Increment static variable directly
MyClass.total_value += 10

# Call different methods to increment static variable
t1.increment_by_non_static_method()
MyClass.increment_by_static_method()
t1.increment_by_class_method()

# Print the final value of the static variable
print(MyClass.total_value)
