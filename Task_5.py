def num_sum():
    sum_1 = 0
    while True:
        numbers_list = input("Enter numbers with space, or 'sum' to get result or 'end' to end").split()
        for i in numbers_list:
            if i == 'end':
                return sum_1
            if i == 'sum':
                print(f"Sum = {sum_1}")
                break
            else:
                sum_1 += int(i)

    return f"Sum = {sum_1}"

num_sum()
