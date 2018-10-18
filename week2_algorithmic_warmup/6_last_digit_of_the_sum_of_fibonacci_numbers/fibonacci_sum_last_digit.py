# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):

    if n <= 1:
        return n

    previous = 0
    current  = 1

    seq = [0, 1]
    for _ in range(n - 1):
        previous, current = current % 10, (previous + current + 1 ) % 10
        if previous == 0 and current == 1:
            break
        seq.append(current)

    seq.pop()

    print(seq)
    return seq[n % len(seq)]

    # for _ in range(n - 1):
    #     previous, current = current % 10, (previous + current + 1 ) % 10

    # return current

def func(n):

    m = 10

    arr = [0, 1]
    sums = [0, 1]
    seq = [0, 1]
    previous = 0
    current = 1
    for _ in range(0, n + 1):
        previous, current = current, previous + current

        if previous % m == 0 and current % m == 1:
            break

        arr.append(current)
        # sums.append(previous + current)
        seq.append(current % m)

    print(arr)
    # print(sums)
    print(seq)
    return seq[(n + 2) % len(seq)] - 1


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_naive(n))
    print(func(n))
