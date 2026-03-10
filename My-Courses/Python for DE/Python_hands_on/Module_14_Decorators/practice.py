



def f1(func):
    def wrapper(*args, **kwargs):
        print('Execution started')
        val = func(*args, **kwargs)
        print('Execution finished')
        return val
    return wrapper

@f1
def f(a):
    print(f'Function printing {a}')

@f1
def sum(a,b):
    return a + b
# print(f1(f)())

# tempFunc = f1(f)  # function aliasing

# tempFunc()

# f('Hii')

print(sum(1,2))