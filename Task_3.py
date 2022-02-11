def max_two(a, b, c):
    max_list = [a, b, c]
    try:
        max_list.remove(min(max_list))
        return sum(max_list)
    except TypeError:
        return "Something wrong"


print(max_two(a=int(input()), b=int(input()), c=int(input())))
