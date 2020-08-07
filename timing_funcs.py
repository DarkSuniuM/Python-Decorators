import time

def time_this_function(f):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        output = f(*args, **kwargs)
        print(time.perf_counter_ns() - start)
        return output
    return wrapper


# @time_this_function
def make_list_using_list_func(iterable):
    return list(iterable)


@time_this_function
def make_list_using_for_loop(iterable):
    return [i for i in iterable]


make_list_using_list_func(range(50))
make_list_using_for_loop(range(50))
