class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Demonstrate inheritance and polymorphism
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
# Modified print statement
    print(animal.speak())

# Demonstrate method overloading
calc = Calculator()
# Modified print statement
print(calc.add(2, 3))       # Output: 5
# Modified print statement
print(calc.add(2, 3, 4))    # Output: 9

'''
# Output:
# Buddy says Woof!
# Whiskers says Meow!
# 5
# 9'''