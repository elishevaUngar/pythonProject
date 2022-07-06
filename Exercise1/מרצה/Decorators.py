import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("start")
        result = func(*args,**kwargs)
        print("end")
        return result

    return wrapper


# print_name = start_end_decorator(print_name)
@start_end_decorator
def add5(x):
    return x + 5
# def print_name():
#     print('Yuri')

# print(help(add5(10)))
print(add5.__name__)
# print(result)



# print_name()

def repeat(num_of_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_of_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_of_times=5)
def greet(name):
    print(f"Hello {name}")


greet('Yuri')