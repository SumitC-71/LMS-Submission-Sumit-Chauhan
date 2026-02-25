'''
Task 9: Copy File Content
    1. Write a Python program to copy the content of students.txt into a new file named 
    students_backup.txt.
'''


source='students.txt'
destination='students_backup.txt'

with open(source,'r') as rf:
    with open(destination,'w') as wf:
        for line in rf:
            wf.write(line)
        print('Backup file created successfully!')