n = int(input("Input number 'n':"))
while n < 0:
    print("Please enter number greater than 0")
    n = int(input("Input number 'n':"))
n2 = int(str(n) + str(n))
n3 = int(str(n) + str(n) + str(n))
total = n + n2 + n3
print(n, "+", n2, "+", n3, "=", total)
