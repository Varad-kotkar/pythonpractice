# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Before Function")
#         func(*args,**kwargs)
#         print("After Function")
#     return wrapper        
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before Function")
        result = func(*args, **kwargs)
        print("After Function")
        return result
    return wrapper




@my_decorator
def introduce(name, age):
    print(f"My name is {name}, age is {age}")


introduce(name="Varad", age=21)

@my_decorator
def add(a, b):
    return a + b
result = add(10, 20)
print(result)