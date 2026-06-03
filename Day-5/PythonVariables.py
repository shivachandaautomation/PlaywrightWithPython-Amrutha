# age = '30'

# print((age))

# name = "shiva"
# print(type(name))

# Operators
# +, -, *, /, %, **, //, =, +=, -=, *=, /=, %=, **=, //=
# Comparison Operators
# print(8!=23)

# name = input("Enter your name: ")
# print(name)
# print("Hello, " + name + "! Welcome to Python programming.")

# Strings

country = "India"
city = 'Bangalore'

# String Indexing

# x = "Hello, World!"
# print(x[0])  # Output: H
# print(x[7])  # Output: W
# print(x[-1]) # Output: !
# print(x[-6]) # Output: W

# String slicing
# String Methods
text = "Python Programming"
print(text[0:6])  # Output: Python
print(text[7:18]) # Output: Programming 
print(len(text)) # Output: 18
print(text[2:]) # Output: thon Programming
print(text[:6]) # Output: Python

text = "Python, Programming"
# String methods:

print(text.upper()) # Output: PYTHON PROGRAMMING
print(text.lower()) # Output: python programming
print(text.capitalize()) # Output: Python programming
print(text.replace("Python", "Java")) # Output: Java Programming
print(text.split(",")) # Output: ['Python', ' Programming']
print(text.strip()) # Output: Python, Programming
print(text.find("Programming")) # Output: 8
print(text.count("o")) # Output: 2
print(text.startswith("Python")) # Output: True
print(text.endswith("Programming")) # Output: True
print(text.isalpha()) # Output: False (because of the comma and space)
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: False (because of the comma and space)
print(text.index("Programming")) # Output: 8
print(text.rindex("o")) # Output: 14
print(text.rfind("o")) # Output: 14

# f-strings
name = "Maya"
age = 28
print(f"{name} is {age} years old") 

#Lists, Tuples, Sets, and Dictionaries
my_list = [1, 2, 3, 4, 5]   
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "Maya", "age": 28}

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)
