from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass
    
    @staticmethod
    def display():
        # Static method to display a message
        print("This is a static method inside the abstract class")

class MyColorButton(Button):
    def click(self):
        # Implementation of the click method for a color button
        print("Color is red")

class MyPhotoButton(Button):
    def click(self):
        # Implementation of the click method for a photo button
        print("This is my photo")

# We cannot create objects of an abstract class directly
# b = Button()

# Creating objects of concrete subclasses
color_button = MyColorButton()
photo_button = MyPhotoButton()

# Calling the click method of each object
color_button.click()
photo_button.click()
