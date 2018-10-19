# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    arr_sum = [0, 1]
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
        arr_sum.append(sum)

    return sum % 10


def fibonacci_sum_fast(n):

    if n <= 1:
        return n

    m = 10
    n += 2
    seq = [0, 1]
    previous = 0
    current = 1
    for _ in range(n):
        previous, current = current, previous + current
        if previous % m == 0 and current % m == 1:
            break
        seq.append(current % m)

    seq.pop()
    if seq[n % len(seq)] == 0:
        return 9
    return seq[n % len(seq)] - 1


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_fast(n))
