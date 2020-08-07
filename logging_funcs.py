def print_log(function):
    def inner_function(*args, **kwargs):
        print(f"Running function '{function.__name__}' with args {args}")
        output = function(*args, **kwargs)
        print('Unreachable')
        return output
    return inner_function


@print_log
def add(x, y):
    return x + y


@print_log
def sub(x, y):
    return x - y


@print_log
def mul(x, y):
    return x * y


@print_log
def div(x, y):
    return x / y


print(add(9, 6))
print(sub(9, 6))
print(mul(9, 6))
print(div(9, 6))
