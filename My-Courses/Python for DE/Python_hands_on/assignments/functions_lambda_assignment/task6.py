'''
6. Decorators
    ● Write a decorator execution_time to calculate and display the time taken by a
    function to execute.
    ● Usethedecorator on a function that calculates the factorial of a large number (e.g.,
    1000).
'''
from functools import lru_cache
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

# custom factorial function with memoization with lru
@lru_cache(None,True)
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

def factorial_without_lru(n):
    if n==1:
        return 1
    return n * factorial(n-1)

@measure_time
def higher_order_function(func,n):
    return func(n)

def main(n):
    runtime = higher_order_function(factorial,n)
    runtime2 = higher_order_function(factorial_without_lru,n)
    print(f'execution time with lru cache: {runtime}')
    print(f'execution time without lru cache: {runtime2}')

main(10)
