def multiply_by(x):
    def multiplier(y):
        return x * y
    return multiplier


multiply_by_2 = multiply_by(2)

for i in range(10):
    print(multiply_by_2(i))
