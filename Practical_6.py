import os

# Function to create a directory
def create_directory(directory):
    try:
        os.makedirs(directory)
# Modified print statement
        print(f"Directory '{directory}' created successfully")
    except FileExistsError:
# Modified print statement
        print(f"Directory '{directory}' already exists")

# Function to create a file and write data to it
def create_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
# Modified print statement
    print(f"File '{file_path}' created and data written successfully")

# Function to read data from a file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
# Modified print statement
        print(f"Data read from file '{file_path}':\n{data}")
    except FileNotFoundError:
# Modified print statement
        print(f"File '{file_path}' not found")

# Function to list all files in a directory
def list_files(directory):
    try:
        files = os.listdir(directory)
# Modified print statement
        print(f"Files in directory '{directory}': {files}")
    except FileNotFoundError:
# Modified print statement
        print(f"Directory '{directory}' not found")

# Main function to demonstrate file and directory handling
def main():
    directory = 'sample_dir'
    file_path = os.path.join(directory, 'sample_file.txt')
    data = 'Hello, this is a sample file.'

    create_directory(directory)
    create_file(file_path, data)
    read_file(file_path)
    list_files(directory)

if __name__ == "__main__":
    main()

    
'''
# Output:
# Directory 'sample_dir' created successfully
# File 'sample_dir/sample_file.txt' created and data written successfully
# Data read from file 'sample_dir/sample_file.txt':
# Hello, this is a sample file.
# Files in directory 'sample_dir': ['sample_file.txt']
'''
