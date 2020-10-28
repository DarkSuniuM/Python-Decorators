def print_function_name(function):
    print(function.__name__)
    return function


@print_function_name()
def add(x, y):
    return x + y




@print_function_name
def sub(x, y):
    return x - y


@print_function_name
def mul(x, y):
    return x * y


@print_function_name
def div(x, y):
    return x / y


print(add(9, 6))
print(sub(9, 6))
print(mul(9, 6))
print(div(9, 6))
