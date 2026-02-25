'''
Task 1: Create a File
1. Write a Python program to create a file named students.txt.
2. Write the following data into the file:
    - Name, Age, Grade 
    - John, 20, A 
    - Alice, 19, B 
    - Mark, 21, A 
    - Sophie, 22, C
'''
content = [
    'Name, Age, Grade \n',
    'John, 20, A \n',
    'Alice, 19, B \n',
    'Mark, 21, A \n',
    'Sophie, 22, C\n'
]

with open('students.txt','w') as wf:
    wf.writelines(content)
    print('done')
    
