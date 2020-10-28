def log_func_args(function):
    def logger(*args, **kwargs):
        print(f"{function.__name__} => {args}, {kwargs}")
        return function(*args, **kwargs)
    return logger


def multiply(x, y):
    return x * y


multiply_with_logs = log_func_args(multiply)
print(multiply_with_logs(5, 6))
