rating = [5, 4, 3, 2, 1]
print(f"Default rating {rating}")
while True:
    value = input("Enter natural value or 'stop' to stop: ")
    x = int(value) if value.isdigit() else float(value) if value.replace('.', '').isdigit() else value
    if type(x) == float or x == 0:
        print("Please enter natural value or 'stop' to stop!!")
    elif value == 'stop':
        print(f"Finally you've got {rating}")
        break
    elif value.isdigit():
        rating.append(int(value))
        rating.sort(reverse=True)
        print(rating)
    elif type(value) == str:
        print("Please enter natural value or 'stop' to stop!!")
