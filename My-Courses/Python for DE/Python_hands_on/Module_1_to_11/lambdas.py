# lambda functions
# also called anonymous functions

# Can have multiple arguments
# Can have only one expression

# syntax-> lambda arguments: expression

# f = lambda a,b: a+b
# print(f(1,1))

# map function is used to accept function and the list
# it basically applies passed function to all the elements of list or tuple or string or range
# map(lambda function, list)

# lst = range(10)
# square = lambda x: x*x
# sqr = list(map(square, lst))
# print(sqr)

# lambda with filter
# filter function syntax: filter(lambda functions, sequence)
# here lambda functions expression are generally a filter conditions
# return value: boolian
# if True includes that element otherwise excludes it
# it does not change the value of it like map

# lst = range(10)
# square = lambda x: x%2 == 0
# evens = list(filter(square, lst))
# print(evens)

# lambda with reduce
# reduce function reduces or compresses the result 
# it returns single argument instead of sequence
# lambda function syntax: lambda curr, ele: ele - curr
# here ele is the element of sequence in current iteration
# and curr is the current value of result 
# after all iterations are done, this curr will be returned

# from functools import reduce

# lst = range(3)
# lmd = lambda curr, ele: ele - curr
# res = reduce(lmd,lst)
# print(res)

# lambda with sorted
# students = [
#     {"name": "A", "marks": 80},
#     {"name": "B", "marks": 95},
#     {"name": "C", "marks": 70}
# ]

# # sorting based on marks
# sorted_students = sorted(students, key=lambda x: x["marks"])

# lambda with if statements
# lmd = lambda x: "Even" if x%2 == 0 else "Odd"
# print(lmd(6))

# lambdas are not faster than functions, its just syntacally different

# we can use tuples to return multiple expressions
# lmd = lambda x,y: (x+y,x-y)
# print(lmd(2,2))

