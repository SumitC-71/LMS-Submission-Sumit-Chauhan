'''
Task 5: Update the File
    1. Write a Python program to update the age of 'Sophie' to 23 in the students.txt file.
    2. Save the updated data back to the file
'''
import csv
# TODO: handle the header, map header name with index

rows=[]
with open('students.txt','r') as rf:
    reader = csv.reader(rf)
    for row in reader:

        # find row with name Sophie and update age
        if row[0].strip() == 'Sophie':
            row[1]=23
        rows.append(row)

# newline parameter specifically used when working with csv
# write out stored lines
with open('students.txt','w',newline="") as wf:
    writer = csv.writer(wf)
    writer.writerows(rows)
