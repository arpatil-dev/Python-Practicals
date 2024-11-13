class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Modified print statement
        print(f"Person {self.name} is created.")

    # Method to display person's details
    def display(self):
# Modified print statement
        print(f"Name: {self.name}, Age: {self.age}")

    # Destructor
    def __del__(self):
# Modified print statement
        print(f"Person {self.name} is destroyed.")

# Creating an object of the Person class
person1 = Person("Pawan", 20)

# Displaying the details of person1
person1.display()

# Deleting the person1 object
del person1

'''
# Output
# Person Pawan is created.
# Name: Pawan, Age: 20
'''
