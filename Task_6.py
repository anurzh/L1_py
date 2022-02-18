def int_func():
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]


source = input().split()
res = []
for word in source:
    res.append(int_func())
print(' '.join(res))