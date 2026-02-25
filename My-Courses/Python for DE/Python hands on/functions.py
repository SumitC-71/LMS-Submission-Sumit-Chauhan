def greet(name='sumit'):
    print(f'Hello, {name}!')

greet()
greet('yuval')

# default parameters 

def add(x,y):
    return x+y
print(add(2,2))
print(add(y=2,x=2)) # keyword arguments
# when you don't return anything, function returns None

def add_sub(x,y): 
    return x+y, x-y   # returns tuple of (x+y,x-y)
print(add(2,2))

a,b = add_sub(2,2)
print(add_sub(2,2)) # will not throw error but prints tuple
print(a,b)

# recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# type strict function parameters and return statements
print(add('sumit ','chauhan')) # will perform concatation

def add_(a: int,b: int) -> int:
    return a+b
# note that this only gives hint to developers that they are supposed to pass only int arguments and that return value should be int

print(add_(2,2))
print(add_('sumit ','chauhan'))  

# variable arguments
def avg(*numbers):  # * means tuple
    return sum(numbers)/len(numbers)
print(avg(1,1,1))

def print_info(**data): # ** means dictionary
    print(data.get('name'))

print_info(name='sumit',age='22')


