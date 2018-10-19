# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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


def fibonacci_partial_sum_fast(from_, to):

    left = get_fibonacci_modulo(from_ + 1, 10)
    right = get_fibonacci_modulo(to + 2, 10)

    return (right + 10 - left) % 10

if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))