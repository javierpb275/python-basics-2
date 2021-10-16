# *args **kwargs

def super_func(*args, **kwargs):
    print(args)  # (1, 2, 3, 4, 5)
    print(*args)  # 1 2 3 4 5
    total = 0
    print(kwargs)  # {'num1': 6, 'num2': 7}
    for item in kwargs.values():
        total += item
    return sum(args) + total  # 28


# args: 1, 2... 5; kwargs: 6, 7
total = super_func(1, 2, 3, 4, 5, num1=6, num2=7)

print(total)  # 28

# Rule: params, *args, default parameters, **kwargs
def super_func_2(name, *args, i='hi', **kwargs):
    pass

super_func_2('pepe', 1, 2, 3, 4, 5, num1=6, num2=7)