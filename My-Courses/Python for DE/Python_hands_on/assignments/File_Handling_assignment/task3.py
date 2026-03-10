'''
Task 3: Append Data to the File
    1. Add the following data to the students.txt file:
        Emma, 20, B
        Liam, 23, A
    2.   Ensure that the new data is appended without overwriting the existing content.
'''

lines = [
    'Emma, 20, B\n',
    'Liam, 23, A\n'
]
with open('students.txt','a') as af:
    af.writelines(lines)