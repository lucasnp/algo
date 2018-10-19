# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def func(n, m):

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

if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    print(func(n, m))
