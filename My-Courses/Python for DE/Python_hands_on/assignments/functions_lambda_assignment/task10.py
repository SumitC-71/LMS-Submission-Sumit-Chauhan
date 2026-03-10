'''
10. Real-World Use Case: Dynamic Function Application
● Write a function dynamic_function that:
    ○ Takesalist of numbers and a string indicating the operation ("add",
"subtract", "multiply", "divide").
    ○ Dynamically applies the operation using lambda functions.
    ○ Returns the result of applying the operation to all numbers in the list.
● Test it with various lists and operations.
'''
from functools import reduce

# defining map of named lambda functions
operations = {
    "add": lambda cur,ele: cur+ele
    , "subtract": lambda cur,ele: cur-ele
    , "multiply": lambda cur,ele: cur*ele
    , "divide": lambda cur,ele: cur/ele
}

# dynamic function that accepts list and operation name
def dynamic_function(lst,operation):
    return reduce(operations[operation],lst)

lst = [24,2,3,4]
# print(dynamic_function(lst,'add'))
# print(dynamic_function(lst,'subtract'))
# print(dynamic_function(lst,'multiply'))
# print(dynamic_function(lst,'divide'))

# iterating through all operations
for operation in operations:
    print(f'{operation} operation result: {dynamic_function(lst,operation)}')
