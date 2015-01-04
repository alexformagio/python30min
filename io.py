__author__ = 'formagio'

import os

# FILE I/O -------------

# Overwrite or create a file for writing
test_file = open("/home/formagio/test.txt", "wb")

# Get the file mode used
print(test_file.mode)

# Get the files name
print(test_file.name)

# Write text to a file with a newline
test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# Close the file
test_file.close()

# Opens a file for reading and writing
test_file = open("/home/formagio/test.txt", "r+")

# Read text from the file
text_in_file = test_file.read()

print(text_in_file)

# Delete the file
os.remove("/home/formagio/test.txt")

