
def integer_args_only(function):
    def wrapper(*args, **kwargs):
        try:
            args = [int(i) for i in args]
        except ValueError:
            return 0
        return function(*args, **kwargs)
    return wrapper


@integer_args_only
def add(x, y):
    return x + y


@integer_args_only
def sub(x, y):
    return x - y


@integer_args_only
def mul(x, y):
    return x * y


@integer_args_only
def div(x, y):
    if y == 0:
        return 0
    return x / y

print(add(9, '6s'))
print(sub(9, 6))
print(mul(9, 6))
print(div(9, 6))
