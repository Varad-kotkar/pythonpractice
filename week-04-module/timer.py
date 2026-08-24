# pip install functools
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Function started")
        # result= func(*args,**kwargs)
        print("Function finished")
        return func(*args,**kwargs)
    return wrapper


@timer
def add(a, b):
    return a + b

print(add(10, 20))