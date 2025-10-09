def fib(pos):
    #defines the first 2 numbers in the sequence
    sequence = [0, 1]
    if pos < 1:
        return 0
    elif pos == 1 or pos == 2:
        return sequence[pos-1]
    else:
        for num in range(pos-2):
            sequence = [sequence[1], (sequence[0] + sequence[1])]
        return sequence[1]