def fibonacci(n):
    sequence = [0, 1]
    if n <= 1:
        return n

    for _ in range(2, n):
        sequence.append(sequence[_ - 1] + sequence[_ - 2])
        print(sequence)

    return sequence[-1] + sequence[-2]

hi = fibonacci(5)
print(hi)
