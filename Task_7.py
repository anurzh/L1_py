def generator(number):
    factorial = 1
    for i in range(factorial + number):
        yield f'{i}! = {factorial}'
        factorial *= i + 1


for el in generator(int(input('Input factorial number: '))):
    print(el)
