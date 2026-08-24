# def login_required(func):
#     def is_logged_in(*args, **kwargs):
#         if is_logged_in == True:
#             result = func(*args, **kwargs)

#         else:
#             print("Please login first.")
#     return is_logged_in

is_logged_in = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if is_logged_in == True:
            result = func(*args, **kwargs)
            return result
        else:
            print("Please login first.")
    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()

is_logged_in = True

@login_required
def view_profile(name):
    print(f"Welcome {name}")

view_profile("Varad")