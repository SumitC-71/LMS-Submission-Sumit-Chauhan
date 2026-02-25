'''
Task 2: Read the File
    1. Write a Python program to read the students.txt file and display its content on the 
    console.
    2. Split the content line by line and print each line separately
'''

with open('students.txt','r') as rf:
    content = rf.read()
    print(f'content:\n{content}')

    # reset file pointer
    rf.seek(0)

    # content line by line
    print(f'content line by line:')
    line_no=0
    for line in rf:
        print(f'line {line_no}: {line}',end='')
        line_no+=1
