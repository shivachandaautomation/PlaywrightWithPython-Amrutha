import os
import datetime
import math
datetime_object = datetime.datetime.now()
# print(datetime_object)
# python pythonfunctions.py
# Python functions are reusable blocks of code that perform a specific task. They allow you to break your code into smaller, modular pieces, making it easier to read and maintain. Here are some key points about Python functions:
# 1. Defining a function: You can define a function using the def keyword, followed by the function name and parentheses. Inside the parentheses, you can specify parameters that the function can accept.
# Common Python built-in functions
# print() - display output
# len() - get length of sequences/collections
# type() - inspect object type
# str(), int(), float() - convert types
# range() - generate numeric sequences
# enumerate() - iterate with index
# zip() - combine iterables pairwise
# sorted() - sort items
# min(), max() - find smallest/largest value
# sum() - add numeric items
# map(), filter() - transform and filter iterables
# open() - read/write files
# input() - read user input
# abs() - absolute value
# all(), any() - boolean checks across iterables
# isinstance() - type/class checking
# Example of a simple function in Python:
def greet(name):
    print(f"Hello, {name}!")

greet("India")  # Output: Hello, India! 

def sum(a, b, c=3):
    return a + b + c

result = sum(50,8)  # Output: 63
print(result)  # Output: 63
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

result = calculate_area(5)
print(result)  # Output: 78.53981633974483

def get_current_datetime():
    return datetime.datetime.now()

result = get_current_datetime()
print(result)  # Output: 2023-10-10 12:00:00.000000 

