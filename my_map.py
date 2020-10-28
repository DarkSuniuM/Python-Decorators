def my_map(function, iterable):
    for each in iterable:
        yield function(each)

array = [i for i in range(10)]

print("Using lambda")
print(list(my_map(lambda x: x * 2, array)))

def my_function(x):
    return x * 2

print("Using my_function")
print(list(my_map(my_function, array)))
