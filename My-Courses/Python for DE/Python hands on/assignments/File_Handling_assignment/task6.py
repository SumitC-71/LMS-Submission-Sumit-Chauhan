'''
Task 6: Work with Large Files
    1. Create a file named numbers.txt and write numbers from 1 to 1000, each on a new 
    line.
    2. Write a Python program to:
        ○ Read the file.
        ○ Calculate and display the sum of all numbers in the file.
'''

with open('numbers.txt','w') as wf:

    # note: with w mode as well, with loops we get 1000 lines, 
    # its strange to have new lines after write operation
    for num in range(1000):
        wf.write(str(num+1)+'\n')

with open('numbers.txt','r') as rf:
    sum=0
    try:
        for num in rf:
            sum += int(num)
    except TypeError:
        print('File contains non-numeric characters')
    print(sum)

