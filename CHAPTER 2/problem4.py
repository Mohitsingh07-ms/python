import os

# Specify the directory path
path = '/New folder'

# Print the contents of the directory
for item in os.listdir(path):
    print(item)