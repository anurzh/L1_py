sentence = input("Enter any sentence or words: ")
splt_sentence = sentence.split()
j = 0
for i in splt_sentence:
    print(f'{j}. {splt_sentence[j]:.10s}')
    j += 1

