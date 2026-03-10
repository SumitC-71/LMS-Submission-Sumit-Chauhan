import time

def timer(func):
    def wrapper(*args, **kwargs):
        begin = time.perf_counter() 
        val = func(*args, **kwargs)
        print(f'\nFunction took: {time.perf_counter() - begin} seconds to run')
        return val
    return wrapper

@timer
def sleeper(sec):
    for i in range(sec):
        print('. ',end='')
        time.sleep(1)

sleeper(3)