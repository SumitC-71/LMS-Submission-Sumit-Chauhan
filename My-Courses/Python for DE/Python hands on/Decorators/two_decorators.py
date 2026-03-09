import time

def f1(func):
    def wrapper(*args, **kwargs):
        print('Execution started')
        val = func(*args, **kwargs)
        print('Execution finished')
        return val
    return wrapper
def f2(func):
    def wrapper(*args, **kwargs):
        print('Execution started ----')
        val = func(*args, **kwargs)
        print('Execution finished ----')
        return val
    return wrapper

@f1
@f2
def sleeper(sec):
    for i in range(sec):
        print('. ',end='')
        time.sleep(1)

# say_hello = deco1(deco2(say_hello))