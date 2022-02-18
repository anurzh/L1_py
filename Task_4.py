def pow_func(x, y):
    if type(x) == type(1.1) and y <= 0:
        result = x ** y
    else:
        print("Enter float and negative numbers")
    return result


print(pow_func(x=float(input()), y=int(input())))
