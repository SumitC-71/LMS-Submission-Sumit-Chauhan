'''
Task 4: Analyze the File
    1. Write a Python program to count and display:
        ○ The total number of students in the file.
        ○ The number of students who received a grade 'A'
'''

import csv

with open('students.txt','r') as rf:
    # calculating total lines with readlines
    # -1 for excluding header line from count
    total_lines= len(rf.readlines()) - 1
    print(f'total lines: {total_lines}')

    # resets file pointer
    rf.seek(0)
    
    # using csv to seperate out things with comma(,)
    reader = csv.reader(rf)

    total_students_with_A_grade=0
    for row in reader:
        if row[2].strip() == 'A':
            total_students_with_A_grade += 1
    print(f'total students who got grade A: {total_students_with_A_grade}')


