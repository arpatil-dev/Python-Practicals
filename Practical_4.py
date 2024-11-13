# Demonstrating Set
my_set = {1, 2, 3, 4, 5}
# Modified print statement
print("Original Set:", my_set)

# Adding an element to the set
my_set.add(6)
# Modified print statement
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
# Modified print statement
print("Set after removing an element:", my_set)

# Demonstrating Dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Modified print statement
print("\nOriginal Dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict['email'] = 'alice@example.com'
# Modified print statement
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['age']
# Modified print statement
print("Dictionary after removing a key-value pair:", my_dict)

# Demonstrating String
my_string = "Hello, World!"
# Modified print statement
print("\nOriginal String:", my_string)

# Converting string to uppercase
upper_string = my_string.upper()
# Modified print statement
print("String in uppercase:", upper_string)

# Replacing a substring in the string
replaced_string = my_string.replace("World", "Python")
# Modified print statement
print("String after replacement:", replaced_string)

""" 
Output:

Original Set: {1, 2, 3, 4, 5}
Set after adding an element: {1, 2, 3, 4, 5, 6}
Set after removing an element: {1, 2, 4, 5, 6}

Original Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
Dictionary after adding a key-value pair: {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
Dictionary after removing a key-value pair: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}

Original String: Hello, World!
String in uppercase: HELLO, WORLD!
String after replacement: Hello, Python!
"""