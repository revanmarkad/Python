class Country:
    def __init__(self):
        print("Initializing country")

    def displayCountry(self):
        print("Displaying country")

    class State:
        def __init__(self):
            print("Initializing state")

        def displayState(self):
            print("Displaying state")

        class City:
            def __init__(self):
                print("Initializing city")

            def displayCity(self):
                print("Displaying city")



# Creating an instance of the outer class Country
country_instance = Country()

# Calling methods of the outer class
country_instance.displayCountry()

# Creating an instance of the inner class State
state_instance = country_instance.State()

# Calling methods of the inner class
state_instance.displayState()

# Creating an instance of the innermost class City
city_instance = state_instance.City()

# Calling methods of the innermost class
city_instance.displayCity()
