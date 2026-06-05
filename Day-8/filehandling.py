# python filehandling.py
# File handling in Python allows you to read from and write to files. Here are some common file handling operations:
# 1. Opening a file: You can use the open() function to open a file. It takes two arguments: the file name and the mode (e.g., 'r' for reading, 'w' for writing, 'a' for appending).
# 2. Reading from a file: You can use methods like read(), readline(), or readlines() to read the contents of a file.
# 3. Writing to a file: You can use the write() method to write data to a file.
# 4. Closing a file: It's important to close a file after you're done with it using the close() method, or you can use a with statement to automatically handle this.
# Example of file handling in Python:
# import os

# # open to a file
# file_path = os.path.join(os.path.dirname(__file__), 'namesofemployees')
# file = open(file_path, 'r')
# # file = open(file_path, 'w')
# # file = open(file_path, 'a')
# # file = open(file_path, 'a+')

import os

# open the existing employee names file in the same directory as this script
file_path = os.path.join(os.path.dirname(__file__), 'namesofemployees.txt')
file = open(file_path, 'r+')  # Open the file for reading and writing
file.write("John Doe")
file.write("Jane Smith")
file.write("Alice Johnson")
content = file.read()
print(content)  
file.close()
