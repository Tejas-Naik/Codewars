def find_missing(sequence):
    sequence_difference = []
    for i in range(sequence[0], sequence[-1]+1, sequence[2]-sequence[1]):
        sequence_difference.append(i)

    answer = set(sequence_difference).difference(sequence)
    for a in answer:
        return a

print(find_missing([10, 20, 30, 40, 60]))
