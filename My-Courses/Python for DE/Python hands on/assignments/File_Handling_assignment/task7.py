'''
Task 7: Error Handling
1. Write a Python program to handle the following scenarios:
    ○ Attempt to read a file named non_existent_file.txt and handle the 
    FileNotFoundError.
    ○ Handle other potential exceptions that may arise during file operations.
'''

# Task 7: Error Handling

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)

except FileNotFoundError:
    print("Error: The file 'non_existent_file.txt' was not found.")

except PermissionError:
    print("Error: You don't have permission to access this file.")

except IOError:
    print("Error: An I/O error occurred while handling the file.")

except Exception as e:
    print(f"Unexpected error occurred: {e}")

finally:
    print("File operation attempt completed.")