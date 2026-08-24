def positive_only(func):
    def wrapper(*args):
            # for i in args:
                # if i >0:
        if args[0] > 0:
            result = func(*args)
            return result
        else:
            return "Number must be positive.."
    return wrapper



@positive_only
def square(num):
    return num * num

print(square(-5))