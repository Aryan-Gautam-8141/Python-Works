import os

def print_directory_contents(path):
    try:
        entries = os.listdir(path)  # list all files & directories
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return

    print(f"Contents of directory: {path}")
    for name in entries:
        print(name)

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    print_directory_contents(dir_path)
