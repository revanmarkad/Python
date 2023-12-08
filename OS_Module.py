import os

def list_files_in_directory():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)

    print("Files in the current directory:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

# Call the function to list files in the current directory
list_files_in_directory()
