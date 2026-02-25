'''
Task 10: Delete a File
    1. Write a Python program to delete the file students_backup.txt after confirming from 
    the user.
'''

import os

filename='students_backup.txt'

choice = str(input(f'Are you sure, you want to delete {filename}? [y/n]: '))

if choice == 'y':
    try:
        os.remove(filename)
        print(f'{filename} removed successfully')
    except FileNotFoundError:
        print('Error: File not found')
    except PermissionError:
        print('Permission Error')
    except Exception as e:
        print(f'Unexpected error: {e}')