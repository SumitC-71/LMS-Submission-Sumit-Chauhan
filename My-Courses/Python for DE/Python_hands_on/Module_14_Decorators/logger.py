import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        with open('log.txt','a') as f:
            f.write(f'LOG: function {func.__name__} with {" ".join([str(arg) for arg in args])} arguments and returning {val}\n')
        return val
    return wrapper

@logger
def sum(a,b=34):
    return a+b

print(sum(1,2))
