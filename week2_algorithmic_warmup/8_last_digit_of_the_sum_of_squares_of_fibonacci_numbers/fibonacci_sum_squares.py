# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def get_fibonacci_modulo(n, m):

    if m <= 1:
        return m

    seq = [0, 1]
    previous = 0
    current = 1
    for _ in range(n):
        previous, current = current, previous + current
        if previous % m == 0 and current % m == 1:
            break
        seq.append(current % m)

    seq.pop()

    return seq[n % len(seq)]

def fibonacci_sum_squares_fast(n):

    left = get_fibonacci_modulo(n, 10)
    right = get_fibonacci_modulo(n + 1, 10)

    return left * right % 10

if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares_fast(n))
