'''
3. Recursive Function
    ● Write a recursive function fibonacci that generates the nth Fibonacci number.
    ● Test the function for inputs 10, 15, and 20.
    ● Bonus: Optimize the function using memoization (e.g., with functools.lru_cache)
'''

from functools import lru_cache
import time

@lru_cache(None, True)
def fibonacci(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

print(f'10th fibonacci number: {fibonacci(10)}')
print(f'15th fibonacci number: {fibonacci(15)}')
start = time.perf_counter()
print(f'20th fibonacci number: {fibonacci(20)}')
end = time.perf_counter()
print(f'execution time: {end-start} seconds')

# for running fib(20)
# time with  no cache: 0.0014391000004252419
# time with lru cache: 0.00012400000196066685