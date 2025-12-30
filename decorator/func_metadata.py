from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before call")
        print(f"Function name : {wrapper.__name__}")
        print(f"Doc string : {wrapper.__doc__}")
        print(f"Module name : {wrapper.__module__}")
        print(f"Annotations : {wrapper.__annotations__}")
        print(f"Wrapper : {wrapper.__wrapped__}")
        return func(*args, **kwargs)
        print("After call")
    return wrapper

@my_decorator
def add(a:int,b:int) -> int:
    """Adds two numbers"""
    return a+b

print(add(5,6))