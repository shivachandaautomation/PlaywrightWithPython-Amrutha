# Opening a file in read mode
# file = open("example.txt", "r")

# with open("Python_Training\\example.txt", "r") as file:
#    content = file.read()
#    print(content)
#    F:\\Playwright_Project\\Python_Training\\example.txt

# with open("python_Training\\example.txt", "r") as file:
#    line = file.readline()
#    while line:
#     #   print(line)
#       print(line, end='')
#     # line = file.readline()

# with open("python_Training\\example.txt", "r") as file:
#    lines = file.readlines()
# #    print(lines)
#    for line in lines:
#       print(line, end='')

# with open("python_Training\\example.txt", "r+") as file:
#    file.write("Hello, World!")
#    file.seek(0)
#    lines = file.readlines()
#    print ("Content added Successfully!!")
#    print(lines)

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("python_Training\\example.txt", "w") as file:
   file.writelines(lines)
   print

   # Handling Exceptions When Closing a File

# In Python, we use a try-finally block to handle exceptions when closing a file. The "finally" block ensures that the file is closed regardless of whether an error occurs in the try block −
try:
   file = open("example.txt", "w")
   file.write("This is an example with exception handling.")
finally:
   file.close()
   print ("File closed successfully!!")
