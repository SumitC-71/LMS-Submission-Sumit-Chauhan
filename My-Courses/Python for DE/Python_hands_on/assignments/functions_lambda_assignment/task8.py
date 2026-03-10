'''
8. Functional Programming: Custom Aggregation
    ● Write a function custom_aggregate that:
        ○ Takesalist of numbers and a function as arguments.
        ○ Applies the function to all numbers and returns their aggregated result (e.g., sum,
        product, etc.).
    ● Test it with:
        ○ Alambdafunction that calculates the sum.
        ○ Alambdafunction that calculates the product
'''
from functools import reduce

# lambda functions
sum_func = lambda cur,ele: cur+ele
prod_func = lambda cur,ele: cur*ele

# customizable aggregator function
def aggregator(lst, aggregation_function):
    result = (reduce(aggregation_function,lst))
    return result

lst = [1,2,3,4]
print('sum: ',aggregator(lst,sum_func))
print('product: ',aggregator(lst,prod_func))