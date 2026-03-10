

def decorator(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return val
    return wrapper