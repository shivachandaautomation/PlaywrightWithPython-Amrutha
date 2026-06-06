import time 
import math
from tokenize import String
time.sleep(5)

print("Shiva")

a = 10
b = 20.6
c = "shiva"

c= a+b
print("The sum of a and b is:", c)

for i in range(5):
    k = 10
    print("Iteration:", i)

def add_two_digits(num1, num2):

    return num1 + num2

def subtract_two_digits(num1, num2):
    return num1 - num2

class Calculator:
    def __init__(self,num1):
        self.name = "Simple Calculator"
    name = "Simple Calculator"
    constants = {
        "PI": 3.14159,
        "E": 2.71828
    }

    def add(self, num1, num2):
        marks = 200
        return num1 + num2
    def add(self, a,b,constant_name):
        return self.constants.get(constant_name, "Constant not found")
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2): 
        return num1 * num2   

calc = Calculator()  
result_add = calc.add(5, 3) 
result_subtract = calc.subtract(5, 3)
result_multiply = calc.multiply(5, 3)

class AbstractCalculator:
    def add(self, num1, num2):
        pass

    def subtract(self, num1, num2):
        pass

    def multiply(self, num1, num2):
        pass

    #Dynamic Typing**: Python is dynamically typed language. This means that we are not required to declare the data types of variables explicitly. 
    # For example, x = 10 is an integer, but assigning x = "hello" later changes it to a string.

    #Virtual Environments: Python supports virtual environments (venv) which helps isolating the dependencies for different projects. This also helps preventing package conflicts and ensuring each project runs with the required library versions.

    #PEP 8: Python's official style guide promotes best practices such as meaningful variable names, consistent indentation, proper spacing, and a 79-character line limit for better code readability and maintainability.

What is Python Syntax?
Python syntax is like the grammar of the Python language. It defines how statements are written so that the Python interpreter can understand and execute them correctly. Proper syntax helps in writing structured, readable, and error-free code.

Python Interactive and Script Modes
1. Interactive Mode
2. Script Mode









