'''
exception: FileNotFoundError
'''
# f = open('run.txt','r')
# print(f.mode)
# f.close()  # close the files other wise you may reach limit of maximum allowed open files on system


# context manager
# the benefit of context manager is that whatever you want to do with file you can do in this block 
# and if some exception occurs file will be closed by context manager 
# with open('run.txt','r') as f:
    # f_content = f.read() # reads all the content, dangerous if file is large
    # print(f_content)

    # lines = f.readlines() # returns the list of lines
    # print(lines)

    # line = f.readline()  # returns one line and move the pointer to next line so next time returns the next line
    # print(line,end='')
    # line = f.readline()
    # print(line)

    # reading all lines with for loop
    # for line in f:
    #     print(line,end='')  # this for loop reads all the lines so next time you run a loop or raadline it will be empty

    # line = f.readline()
    # print(f'line: {line}',end='')

    # when you reach EOF (end of file)  f will return empty string

    # chunk = f.read(10)   # reads 10 characters from the file and moves the pointer to next next coming char
    # print(chunk)

    # line = f.readline()
    # print(line)

    # print(f.tell())  # tells on which character currently pointer point to

    # f.seek(0)   # sets the file pointer to 0th position

    # pass

# print(f.closed) # though f is closed, you can access it but you can not do much out of it (like reading or writing; it will throw an error)

# with open('test3.txt','w') as f:
#     # w overwrites the file but a appends the content to existing file
#     # f.write('Test\nHello world')
#     f.write('Test')
#     f.seek(0)
#     f.write('R')
#     pass

# reading and writing at the same time
# with open('test2.txt','r') as rf:
#     with open('textfile_copy','w') as wf:
#         for line in rf:
#             wf.write(line) # this works fine


# # for binary files like images
# with open('photo.jpeg','rb') as rf:
#     with open('binary_copy','wb') as wf:
#         for line in rf:
#             wf.write(line) # this works fine
    
