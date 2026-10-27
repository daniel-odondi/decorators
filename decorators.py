import time

#Decorators enhance the functionality of a function
# Create a normal function
def greet():
    print("Hello, welcome to python decorators")

# Create a decorator


def my_decorator(func):
    def wrapper():
        print("Before the function runs ooo")
        func()
        print("After the function runs")
    return wrapper


greet = my_decorator(greet)
greet()

print(".......................................................")

# The @ Decorator syntax


def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator
def greet():
    print("Hey, Decorators add functionality")


greet()

print("...........................................")
# Practical example - measuring execution time
# Import time


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Execution time: {end - start: .4f} seconds")
        return result
    return wrapper


@timer
def culculate():
    total = sum(range(1_000_000))
    print(total)


culculate()
