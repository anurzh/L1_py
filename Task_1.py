def divide(a, b):
    try:
        num_div = int(a) / int(b)
    except ValueError:
        return "Erorr"
    return (num_div)


print(divide(input("Enter number:"), input("Enter one more number:")))
