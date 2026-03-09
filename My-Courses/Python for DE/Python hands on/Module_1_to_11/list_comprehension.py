'''
shorter syntax 
faster in comparison to normal for loop appending items to list
reason: every time append method needs to be called, but list comprehensions does not contain 
general syntax: lst = [expression for item in iterable if condition == true]



'''

# example without if condition
# the title method of str capitalize first letter of each word
# capitalize method only capitalize first letter of whole string

# animals = ['lion', 'tiger', 'dog', 'cat']
# animal_copy = [animal.title() for animal in animals] 
# print(animal_copy)

# full_name = 'sumit chauhan hello'
# print(full_name.capitalize())


# with if statement
# nums = [1,2,3,4,5]
# odds = [num for num in nums if num % 2 == 1 ]
# print(odds)


# with if-else statement (the order is reversed)
# nums = [1,2,3,4,5]
# odds = [num if num%2==1 else num+1 for num in nums]
# print(odds)


# flattening 2D list
# matrix = [[1,2,3],[4,5,6]]
# flat = [num if num %2 ==0 else 2*num for row in matrix for num in row ]
# oddEven = ['Even' if num %2 ==0 else 'Odd' for row in matrix for num in row ]
# print(flat)

import random

random_list = [(int)(random.random()*10) for i in range(10)]
print(random_list)


'''
Dictionary comprehension:
d = {key_expression: value_expression for item in iterable}

marks = {"A": 80, "B": 60, "C": 40}

updated = {k: v+5 for k, v in marks.items()}
print(updated)

Set comprehension: 
{expression for item in iterable}

'''
# records = ["A", "B", "A", "C"]
# # unique_records = {r for r in records}
# unique_records = set(records)
# print(unique_records)