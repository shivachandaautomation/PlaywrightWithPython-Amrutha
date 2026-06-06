import os
# print(os.getcwd())

# Opening a file in read mode
# file = open("example.txt", "r")

# # Opening a file in write mode
# file = open("example.txt", "w")

# # Opening a file in append mode
# file = open("example.txt", "a")

# # Opening a file in binary read mode
# file = open("example.txt", "rb")

#############################
# Open a file
# fo = open("example.txt", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not: ", fo.closed)
# print ("Opening mode: ", fo.mode)
# fo.close()

##################
# read() − Reads the entire file.

# readline() − Reads one line at a time.

# readlines − Reads all lines into a list.

# with open("python_Training\\example.txt", "r") as file:
#    content = file.read()
#    print(content)

   ###########################

# with open("python_Training\\example.txt", "r") as file:
#    line = file.readline()
#    while line:
#       print(line, end='')
#       line = file.readline()

# with open("python_Training\\example.txt", "r") as file:
#    lines = file.readlines()
#    for line in lines:
#       print(line, end='')

# with open("foo.txt", "w") as file:
#    file.write("Hello, World!")
#    print ("Content added Successfully!!")

# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("python_Training\\example.txt", "w") as file:
#    file.writelines(lines)
#    print ("Content added Successfully!!")

# Using "with" Statement for Automatic File Closing

#  the file is automatically closed at the end of the with block, so there is no need to call close() method explicitly −

# Handling Exceptions When Closing a File
# In Python, we use a try-finally block to handle exceptions when closing a file. The "finally" block ensures that the file is closed regardless of whether an error occurs in the try block −
# try:
#    file = open("example.txt", "w")
#    file.write("This is an example with exception handling.")
# finally:
#    file.close()
#    print ("File closed successfully!!")

#################################################
# Exceptions:
# try:
#    fh = open("testfile", "w")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print ("Error: can\'t find file or read data")
# else:
#    print ("Written content in the file successfully")
#    fh.close()


# def func1(integer: int = 0):
#    x = 'i am good'

# func1('10')
# # try:
#    func1()
# except:
#    print("I am in exception block")

# lst1 = [10,20,23]
# print(lst1[3])

dict1 = {'name':'shiva', 'place':'india'}

# print(dict1['class'])
print(dict1.get('class'))
   
   