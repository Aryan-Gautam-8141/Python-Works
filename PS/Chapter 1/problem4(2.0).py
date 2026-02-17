import os

# specify the directory path
directory_path = input("Enter the directory path: ")

# list  all files and directories in the specified path
content=os.listdir(directory_path)

# print the items
for item in content:
    print(item)