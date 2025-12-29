def my_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print("After call")
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b

print(add(5,6))