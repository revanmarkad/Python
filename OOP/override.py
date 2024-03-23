
# When you define multiple methods with the same name in a Python class, only the last one you define is kept. This means that it replaces any previous ones. This is called method overriding.

class LifeCycle:
    def __init__(self):
        print("Initializing LifeCycle - First __init__")

    def __init__(self):
        print("Initializing LifeCycle - Second __init__")

t = LifeCycle()
print(t)


 