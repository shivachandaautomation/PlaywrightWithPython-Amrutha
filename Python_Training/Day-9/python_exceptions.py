try:
    a = 10
    b = 0
    c = a/b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("Program continues after handling the exception.")

diferent exceptions in python:
1. ZeroDivisionError: Raised when you try to divide a number by zero.
2. FileNotFoundError: Raised when you try to open a file that does not exist.
3. ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
4. TypeError: Raised when an operation or function is applied to an object of inappropriate type