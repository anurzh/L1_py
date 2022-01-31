a = int(input("What is your running distance in a first day? "))
b = int(input("At least how many kilometers? "))
i = 1
while a != b:
    print(f"{i} day: {a:.2f}")
    a = a + 0.1 * a
    i += 1
    if a > b:
        print(f"{i} day: {a:.2f}")
        break
print(f"On the {i} day the athlete reached the result - at least {b} km")
