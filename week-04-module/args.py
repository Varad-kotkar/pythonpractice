def my_decorator(func):
    def wrapper(*args):
        print("Before Function")
        func(*args)
        print("After Function")
    return wrapper        


@my_decorator
def add(a, b):
    print(a + b)


add(10, 20)