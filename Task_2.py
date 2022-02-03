lst = list()
i = 0
j = 0
while True:
    lst.append(input("Enter value:"))
    print("To stop, type 'end'")
    if lst[i] == 'end':
        break
    i += 1
lst.pop(i)
print(f"In your entered order: {lst}")
for order in range(len(lst) // 2):
    lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Подсмотрел в интернете
    j += 2
print(f"In changed order: {lst}")
